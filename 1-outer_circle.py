## https://stackoverflow.com/questions/58543750/whats-the-most-simple-way-to-crop-a-circle-thumbnail-from-an-image
from PIL import Image, ImageDraw

filename = 'input_OG.jpg'

# load image
img = Image.open(filename)

# crop image
size = 5645 # basically size of the disc from edge left edge to the end of it - do this by edge / color diff detection?
img_cropped = img.crop((0, 0, size, size))

# create grayscale image with white circle (255) on black background (0)
mask = Image.new('L', img_cropped.size)
mask_draw = ImageDraw.Draw(mask)
width, height = img_cropped.size
mask_draw.ellipse((0, 0, width, height), fill=255)
#mask.show()

# add mask as alpha channel
img_cropped.putalpha(mask)

# save as png which keeps the alpha channel
img_cropped.save('circle.png', quality=20, optimize=True)



# show final image:
#img_cropped.show()
