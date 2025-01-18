import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit('Too many arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few arguments')
else:
    name, extension = sys.argv[1].split('.')
    extension = extension.lower()
    out_name, out_extension = sys.argv[2].split('.')
    out_extension = out_extension.lower()
    if extension != 'jpeg' and extension != 'png' and extension != 'jpg':
        sys.exit('Invalid format')
    if extension != out_extension:
        sys.exit('Output has invalid format')

shirt = Image.open('shirt.png')

try:
    image = Image.open(sys.argv[1])
    crop = ImageOps.fit(image, size=[600, 600], method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    crop.paste(im=shirt, box=None, mask=shirt)
    crop.save(sys.argv[2])
except FileNotFoundError:
    sys.exit('File not found')


