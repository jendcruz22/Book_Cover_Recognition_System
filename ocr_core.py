import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import shutil
import os
import random
import csv 
import string

def ocr_core(filename):
    extractedInformation = tess.pytesseract.image_to_string(Image.open(filename))

    text = extractedInformation.lower().replace(',','').replace(' ','').replace('_','').replace(':','').replace('=','').replace('(','').replace(')','').replace('"','').replace('|','').replace('#','').replace('$','').replace('&','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
    text = text.translate({ord(c): None for c in string.whitespace})
    with open('tess.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for col in row:
                if col==text:
                    return("\nName of the Book: "+row[1]+"Author: "+row[2])

