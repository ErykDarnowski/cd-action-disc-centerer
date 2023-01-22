import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 153, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 96, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 175, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 156, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("Thresh1", "Trackbars", 190, 1000, nothing)
cv2.createTrackbar("Thresh2", "Trackbars", 135, 1000, nothing)

cv2.createTrackbar("hThresh", "Trackbars", 19, 400, nothing)
cv2.createTrackbar("hMinLine", "Trackbars", 20, 100, nothing)
cv2.createTrackbar("hMaxGap", "Trackbars", 1, 100, nothing)

kernel = np.ones((3,3), np.uint8) 

while True:
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    Thresh1 = cv2.getTrackbarPos("Thresh1", "Trackbars")
    Thresh2 = cv2.getTrackbarPos("Thresh2", "Trackbars")
    hThresh = cv2.getTrackbarPos("hThresh", "Trackbars")
    hMinLine = cv2.getTrackbarPos("hMinLine", "Trackbars")
    hMaxGap = cv2.getTrackbarPos("hMaxGap", "Trackbars")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    images = [
        cv2.imread('circle.png', cv2.IMREAD_COLOR),
    ]
    black = np.zeros((50,440))

    for i, img in enumerate(images):
        black = np.zeros((50,440))

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        result = img

        mask = cv2.dilate(mask, kernel, iterations=1)

        lines = cv2.Canny(result, threshold1=Thresh1, threshold2=Thresh2)
        img_dilation = cv2.dilate(lines, kernel, iterations=1) 
        lines[mask>0]=0

        HoughLines = cv2.HoughLinesP(lines, 1, np.pi/180, threshold = hThresh, minLineLength = hMinLine, maxLineGap = hMaxGap)
        if HoughLines is not None:
            for line in HoughLines:
                coords = line[0]
                length = np.ceil(np.sqrt(np.square(coords[2] - coords[0]) + np.square(coords[3] - coords[1])))
                print(f'({coords[0]}, {coords[1]}) ({coords[2]}, {coords[3]}) = {length}')

                cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [0,0,255], 3)
                cv2.line(black, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)

        cv2.imshow(f"Original{i}", img)
        cv2.imshow(f"Lines{i}", lines)
        cv2.waitKey(1)
