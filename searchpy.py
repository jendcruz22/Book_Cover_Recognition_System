import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
# from cv2 import cv2
# import imageio
# import numpy as np
import shutil
import os
import random
import csv 

# img=cv2.imread("7.jpg")
# plt.imshow(img)

image_path_in_colab='img\8.jpg'
extractedInformation = tess.pytesseract.image_to_string(Image.open(image_path_in_colab))
# print(extractedInformation)

  
# csv file name 
tesscsv = "tess.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = []
cols = []
text=extractedInformation.lower().replace(',','').replace(' ','').replace('_','').replace(':','').replace('=','').replace('(','').replace(')','').replace('"','').replace('|','').replace('#','').replace('$','').replace('&','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
# print (text)

import string
text=text.translate({ord(c): None for c in string.whitespace})
# print(text)

import csv

with open('tess.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #text="kennethgloriacopelandonewordgodcanhajgeyourhealth"
    for row in csv_reader:
      for col in row:
        if col==text:
          nob=row[1]
          noa=row[2]
        #   print (nob)
          print("Name of the Book: "+row[1])
          print("Name of the Author: "+row[2])

# reading csv file 
# with open(tesscsv, 'r') as csvfile: 
#     # creating a csv reader object 
#     csvreader = csv.reader(csvfile) 
      
#     # extracting field names through first row 
#     fields = next(csvreader) 
  
#     # extracting each data row one by one 
#     for row in csvreader: 
#         rows.append(row) 
#     for col in csvreader: 
#         cols.append(col)

# n = len(fields)

# for row in rows[:n]: 
#     # parsing each column of a row 
#     for col in row: 
#         if col == text:
#             print("Name of the book: "+row[1]) 
#             print("Author: "+row[2])

# """Main file"""

# # import os
# # from flask import Flask, render_template, request
# import csv
# import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# from PIL import Image
# import string

# # csv file name 
# tesscsv = "tess.csv"
  
# import our OCR function
#from ocr_core import ocr_core

# define a folder to store and later serve the images
# UPLOAD_FOLDER = '/static/uploads/'

# # allow files of a specific type
# ALLOWED_EXTENSIONS = set(['jfif','png', 'jpg', 'jpeg'])

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('upload.html')

# # function to check the file extension
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/',methods=['GET', 'POST'])
# def upload_page():
#     if request.method == 'POST':
#         # check if there is a file in the request
#         if 'file' not in request.files:
#             return render_template('upload.html', msg='No file selected')
#         file = request.files['file']
#         # if no file is selected
#         if file.filename == '':
#             return render_template('upload.html', msg='No file selected')

#         if file and allowed_file(file.filename):

#             # call the OCR function on it
#             img = Image.open(filename)
#             text= tess.image_to_string(img)
#             text=text.lower().replace(',','').replace(' ','').replace('_','').replace(':','').replace('=','').replace('(','').replace(')','').replace('"','').replace('|','').replace('#','').replace('$','').replace('&','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
# #print (text)
#             text=text.translate({ord(c): None for c in string.whitespace})
# #print(text)


#             with open('tess.csv') as csv_file:
#                 csv_reader = csv.reader(csv_file, delimiter=',')
#     #text="kennethgloriacopelandonewordgodcanhajgeyourhealth"
#                 for row in csv_reader:
#                     for col in row:
#                         if col==text:
#                             extracted_text="Name of the book: "+row[1]+"\nAuthor: "+row[2]
#                             #print("Name of the Book: "+row[1])
#                             #print("Name of the Author: "+row[2])                   


#             # extract the text and display it
#             return render_template('upload.html',extracted_text=extracted_text,img_src=UPLOAD_FOLDER + file.filename)
#     elif request.method == 'GET':
#         return render_template('upload.html')

# @app.route('/about/')
# def about():
#     return render_template('about.html')

# if __name__ == '__main__':
#     app.run()