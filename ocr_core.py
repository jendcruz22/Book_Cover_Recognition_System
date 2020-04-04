# try:
#     from PIL import Image
# except ImportError:
#     import Image

# import pytesseract

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def ocr_core(filename):
    img = Image.open(filename)
    text= tess.image_to_string(img)
    return(text)

print(ocr_core('img/example_01.png'))


