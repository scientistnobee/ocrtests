
from PIL import Image
import os
import pytesseract
print pytesseract.image_to_string(Image.open(os.path.abspath(
'Screenshot 2018-11-27 at 18.31.26.jpg')))

