## https://stackoverflow.com/questions/58543750/whats-the-most-simple-way-to-crop-a-circle-thumbnail-from-an-image
# Imports:
from PIL import Image, ImageDraw


# Vars:
filename = 'input.jpg'


# Load image:
img = Image.open(filename)

# Crop image:
size = 5645
img_cropped = img.crop((0, 0, size, size))

# Create grayscale image with white circle (255) on black background (0):
mask = Image.new('L', img_cropped.size)
mask_draw = ImageDraw.Draw(mask)
width, height = img_cropped.size
mask_draw.ellipse((0, 0, width, height), fill=255)
#mask.show()

# Add mask as alpha channel:
img_cropped.putalpha(mask)

# Save as png which keeps the alpha channel:
img_cropped.save('circle.png')


# Show final image:
#img_cropped.show()
