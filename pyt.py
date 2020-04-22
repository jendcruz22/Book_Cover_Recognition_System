import os
from flask import Flask, render_template, request

# import our OCR function
from ocr_core import ocr_core


# importing csv module 
import csv 
  
# csv file name 
tesscsv = "tess.csv"
  
def searches(tesstext):
    # initializing the titles and rows list 
    fields = [] 
    rows = [] 

    # reading csv file 
    with open(tesscsv, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    n = len(fields)
    for row in rows[:n]: 
        # parsing each column of a row 
        for col in row: 
            if col == tesstext:
                print("Name of the book: "+row[1]+"Author: "+row[2])
    

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['jfif','png', 'jpg', 'jpeg'])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            tesstext= ocr_core(file)

            #call the search function on it
            # extracted_text= searches(tesstext)

            # extract the text and display it
            return render_template('upload.html',extracted_text=searches(tesstext),img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()