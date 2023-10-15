## https://stackoverflow.com/questions/61497956/cut-out-a-specific-part-of-an-image-with-opencv-in-python
import cv2
import numpy as np

filename = 'circle.png'

# load image
img = cv2.imread(filename)
# ht, wd, cc = img.shape # getting image rows columns and channels

# read mask as grayscale
mask = cv2.imread('mask/mask.jpg', cv2.IMREAD_GRAYSCALE)

# threshold mask and invert
mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)[1]
mask = 255 - mask
hh, ww = mask.shape # getting image dimensions

# make mask 3 channel -> <https://stackoverflow.com/a/59669649/11749019>
mask = cv2.merge([mask, mask, mask])

# set circle center
cx = 62
cy = 336

# offsets from circle center to bottom of region
dx = -20
dy = -27

# compute top left corner of mask (using size of mask, center and offsets)
left = cx + dx
top = cy + dy - hh

# put mask into black background image
mask2 = np.zeros_like(img)
mask2[top: top + hh, left: left + ww] = mask

# apply mask to image
img_masked = cv2.bitwise_and(img, mask2)

# crop region
img_masked_cropped = img_masked[top: top + hh, left: left + ww]

# ALTERNATE just crop input:
img_cropped = img[top: top + hh, left: left + ww]

# DEBUG
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save result
cv2.imwrite('mask_inserted.jpg', mask2)
