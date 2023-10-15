## https://stackoverflow.com/a/62815139/11749019
# https://stackoverflow.com/a/59669649/11749019
# https://stackoverflow.com/questions/61497956/cut-out-a-specific-part-of-an-image-with-opencv-in-python

"""TODO
- higher resolution mask for cleaner output
- better solution for the transparency?
- figure out and comment what the transparency conversion does
"""

import cv2

# load images as Numpy arrays in BGR order
img_org = cv2.imread('input.jpg')
img_mask = cv2.imread('mask/mask.jpg')

# crop out disc from img
size = 1067 # basically the size of the disc from left edge to where it ends - do this by edge / color diff detection? - 1200 - 133 = 1067 (instead of 5645)
img_org_cropped = img_org[0:size, 0:size]

# apply mask to image (cut out) -> <https://stackoverflow.com/questions/44333605/what-does-bitwise-and-operator-exactly-do-in-opencv>
img_cut = cv2.bitwise_and(img_mask, img_org_cropped)

# change black color to transparency -> <https://stackoverflow.com/questions/40527769/removing-black-background-and-make-transparent-from-grabcut-output-in-python-ope>
tmp = cv2.cvtColor(img_cut, cv2.COLOR_BGR2GRAY)
_, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
b, g, r = cv2.split(img_cut)
rgba = [b, g, r, alpha]
result = cv2.merge(rgba, 4)

# save result
cv2.imwrite('circle.png', result)
