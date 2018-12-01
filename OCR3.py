from PIL import Image
import os
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def ocr(file_to_ocr):
    im = Image.open(file_to_ocr)
    txt=pytesseract.image_to_string(im)
    return txt

directory = "/home/pi/Desktop/Archive"
for root,dirs,files in os.walk(directory):
   for file in files:
      if file.endswith(".jpg"):
         pre_fix=file[:-4]
         txt=ocr(file)
         with open(directory+"\\"+pre_fix+".txt",'w') as f: f.write(str(txt))
