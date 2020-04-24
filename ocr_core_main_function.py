import pytesseract as tess
import string
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('accuracy/images/New folder/14.jpg')
text= tess.image_to_string(img)
# print(text)

text = text.lower().replace(',','').replace('\n',' ').replace('_','').replace(':','').replace('=','').replace('(','').replace(')','').replace('"','').replace('|','').replace('#','').replace('$','').replace('&','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
print(text)
total = 0
 
for i in text:
    total = total + 1
 
print("Total Number of Characters in this String = ", total)
