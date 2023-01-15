## https://stackoverflow.com/questions/61497956/cut-out-a-specific-part-of-an-image-with-opencv-in-python
# Imports:
import cv2
import numpy as np


# Vars:
filename = 'circle.png'


# Loag image:
img = cv2.imread(filename)
ht, wd, cc = img.shape # ?

# Read mask as grayscale:
mask = cv2.imread('die_mask.png', cv2.IMREAD_GRAYSCALE)

# Threshold mask and invert:
mask = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)[1]
mask = 255 - mask
hh, ww = mask.shape

# Make mask 3 channel:
mask = cv2.merge([mask,mask,mask])

# Set circle center:
cx = 62
cy = 336

# Offsets from circle center to bottom of region:
dx = -20
dy = -27

# Compute top left corner of mask using size of mask and center and offsets:
left = cx + dx
top = cy + dy - hh

# Put mask into black background image:
mask2 = np.zeros_like(img)
mask2[top:top+hh, left:left+ww] = mask

# Apply mask to image:
img_masked = cv2.bitwise_and(img, mask2)

# Crop region:
img_masked_cropped = img_masked[top:top+hh, left:left+ww]

# ALTERNATE just crop input:
img_cropped = img[top:top+hh, left:left+ww]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save result:
cv2.imwrite('die_mask_inserted.jpg', mask2)
