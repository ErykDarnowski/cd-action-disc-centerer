## https://stackoverflow.com/questions/58543750/whats-the-most-simple-way-to-crop-a-circle-thumbnail-from-an-image
from PIL import Image, ImageDraw

filename = 'input.jpg'

# load image
img = Image.open(filename)

# crop out square containing disc
size = 1067 # basically the size of the disc from left edge to where it ends - do this by edge / color diff detection?
# 1200 - 133 = 1067 (instead of 5645)
img_cropped = img.crop((0, 0, size, size))

## create grayscale image with white (`255`) circle (that matches up with the disc) on black (`0`) background
#mask = Image.new('L', img_cropped.size)
#mask_draw = ImageDraw.Draw(mask)
#width, height = img_cropped.size
#mask_draw.ellipse((0, 0, width, height), fill=255)
##mask.show()
#
## add the mask as an alpha channel
#img_cropped.putalpha(mask)

# save the image of the cut out disc (as `.png`, cause it supports transparency - the alpha channel)
img_cropped.save('circle.png')

# ---

# resizing the image to debug quicker
#diff = 5148 # amount of **px** reduce the image by
#shape = img_cropped.shape
#resized_img = img_cropped.resize((shape[0] - diff, shape[1] - diff))
#resized_img.save("resized_image.jpg")

""" show fin image (debug)
img_cropped.show()
"""
