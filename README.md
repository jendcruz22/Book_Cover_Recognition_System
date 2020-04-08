pyt.py is the main file. 

upload.html in the templates file will be used to upload the image and it provides the text converted off of it.


ocr_core.py takes the image uploaded in upload.html and uses pytesseract to covert the image and produce the output which is then returned to upload.html and displayed there.
