## `py template_matcher.py --template template.png --map input.jpg --show`
import os
import cv2
import argparse
import numpy as np
from turtle import color
from scipy import ndimage
from matplotlib import pyplot as plt

"""TODO
- fix the hardcoded values / params and so on situation + compare with repo
"""

# cli args setup
parser = argparse.ArgumentParser(description='Template matcher')
parser.add_argument('--template', type=str, default='template.png', action='store', help='The image to be used as template')
parser.add_argument('--map', type=str, default='circle.png', action='store', help='The image to be searched in')
parser.add_argument('--show', action='store_true', help='Shows result image')
parser.add_argument('--save-dir', type=str, default='./', help='Directory in which you desire to save the result image')
args = parser.parse_args()

MIN_MATCH_COUNT = 2

# hardcoded
debug_filename = 'debug.jpg'
output_filename = 'output.png'

def get_matched_coordinates(temp_img, map_img):
    """
    Gets template and map images and returns matched coordinates from the map image

    Parameters
    ----------
    temp_img: image
        image to be used as the template

    map_img: image 
        image for the template to be searched in

    Returns
    ---------
    ndarray
        an array that contains matched coordinates

    """

    # initiate SIFT (Scale-Invariant Feature Transform) detector -> <https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html>
    sift = cv2.SIFT_create()
    """
    The SIFT (Scale-Invariant Feature Transform) algorithm, developed by D.Lowe
    in 2004, is used for detecting and describing local features in images. It
    is scale-invariant, meaning it can find the same features even if the image
    is scaled.
    
    The algorithm is widely used in computer vision tasks like object detection,
    image recognition, and more.
    """

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(temp_img, None)
    kp2, des2 = sift.detectAndCompute(map_img, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # find matches by knn which calculates point distance in 128 dim
    matches = flann.knnMatch(des1, des2, k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    # check if matches threshold was passed
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        # find homography -> <https://en.wikipedia.org/wiki/Homography_(computer_vision)> / <https://en.wikipedia.org/wiki/Homography>
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        """
        In the field of computer vision, a homography is a transformation that maps
        any two images of the same planar surface in space, assuming a pinhole camera
        model. This has practical applications such as image rectification, image
        registration, or determining camera motion—rotation and translation—between
        two images.

        In projective geometry, a homography is an isomorphism of projective spaces,
        induced by an isomorphism of the vector spaces from which the projective spaces
        derive. It is a bijection that maps lines to lines, and thus a collineation.
        This concept was introduced to understand, explain and study visual perspective,
        and the difference in appearance of two plane objects viewed from different points
        of view.
        """

        h, w = temp_img.shape
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M) # matched coordinates


        ## START (my mod)
        cords = np.int32(dst)
        rect = cv2.minAreaRect(dst)

        # go through all coordinates to find index of the highest point
        print("[DEBUG - template info]\n  cords:")

        for i in range(len(cords)):
            print(f"    {cords[i]}")
            if (cords[i][0][1] == cords.min(axis=0)[0][-1]): # match to highest point (lowest `y`) -> <https://stackoverflow.com/questions/35930617/how-to-find-minimum-maximum-values-axis-by-axis-in-numpy-array>
                highest_point_cords = cords[i][0]
                orientation = i

        print("  rect:")
        for i in rect:
            if type(i) is tuple:
                print(f"    {round(i[0])}, {round(i[1])}")
            else:
                print(f"    {round(i)}")

        """
        - better approach to margin and string interpolation?
        - what about name of rect debug
        """

        # get found template's angle -> <https://theailearner.com/tag/cv2-minarearect/>
        angle = rect[-1]

        # add offset to the angle to correct the disc's rotation
        print(f"\n  orientation: {orientation} ({orientation * 90}°)")
        print(f"  detected {round(angle)}°")
        angle += orientation * 90 # angle is the amound of degrees the image needs to be roated (counter-clockwise) or by doing (360 - angle) clockwise
        print(f"  corrected: {round(angle)}°")

        # load og map image
        circle = cv2.imread(args.map, cv2.IMREAD_UNCHANGED)

        # center map image 
        rotated_image = ndimage.rotate(circle, angle, reshape=False)

        # write corrected (centered) image
        cv2.imwrite(os.path.join(output_filename), rotated_image)
        ## END


        # drawing highest point and rectangle around found template on map image
        map_img = cv2.circle(map_img, highest_point_cords, radius=25, color=(0, 0, 255), thickness=8)
        map_img = cv2.polylines(map_img, [cords[0], cords[1], cords[2]], True, 255, 3, cv2.LINE_AA)

        """ debug
        cv2.imshow('circle', map_img)
        cv2.waitKey(0)
        """
    else:
        print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0), singlePointColor=None, matchesMask=matchesMask, flags=2)
    #                  ^ draw matches in green      draw only inliers ^

    # draw template and map image, matches, and keypoints
    img3 = cv2.drawMatches(temp_img, kp1, map_img, kp2, good, None, **draw_params)

    # if `--show` argument used, then show result image
    if args.show:
        plt.imshow(img3, 'gray'), plt.show()

    # result image path
    if (args.save_dir != '' and args.save_dir != './'):
        #                          ubuntu fix ^
        
        # dir cleanup
        if not os.path.exists(args.save_dir):
            os.mkdir(args.save_dir)

        cv2.imwrite(os.path.join(args.save_dir, debug_filename), img3)
    else:
        cv2.imwrite(os.path.join(debug_filename), img3)

    return dst

# ---

if __name__ == "__main__":
    # read images
    temp_img_gray = cv2.imread(args.template, 0)
    map_img_gray = cv2.imread(args.map, 0)

    # equalize histograms
    temp_img_eq = cv2.equalizeHist(temp_img_gray)
    map_img_eq = cv2.equalizeHist(map_img_gray)

    # calculate matched coordinates
    coords = get_matched_coordinates(temp_img_eq, map_img_eq)
