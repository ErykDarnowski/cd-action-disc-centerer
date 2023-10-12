## https://www.geeksforgeeks.org/python-edge-detection-using-pillow/
"""
from PIL import Image, ImageFilter
 
# Opening the image (R prefixed to string in order to deal with '\' in paths)
image = Image.open('circle.png')
width, height = image.size

size = 1200
image = image.crop(((width / 2) - size, (width / 2) - size, (width / 2) + size, (width / 2) + size))
image.show()
 
# Converting the image to grayscale, as edge detection requires input image to be of mode = Grayscale (L)
image = image.convert('L')
 
# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
image = image.filter(ImageFilter.FIND_EDGES)
 
# Saving the Image Under the name Edge_Sample.png
image.save('edge_sample.png')
"""

import cv2
import numpy as np

# Loading image in grayscale:
img = cv2.imread('circle.png', 0)

center = img.shape
x = center[1] - w/2
y = center[0] - h/2
img = img[y:y+h, x:x+w]

blurred_img = cv2.blur(img,ksize=(5,5))
med_val = np.median(img) 
median_pix = 1400
lower = int(max(0 ,0.7*median_pix))
upper = int(min(255,1.3*median_pix))
edges = cv2.Canny(image=img, threshold1=lower,threshold2=upper)

edges = cv2.resize(edges, (960, 960))
cv2.imshow('test', edges)
cv2.waitKey(0)

indices = np.where(edges != [0])
coordinates = zip(indices[0], indices[1])

# cv2.imshow('test', img) 
# cv2.waitKey(0) 
