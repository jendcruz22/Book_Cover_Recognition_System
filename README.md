# Book Recognition System

pyt.py is the main file. 

search.py has the code which allows us to find a string in our CSV file and displays the name of the book and its author

ocr_core.py takes the image uploaded in upload.html and uses pytesseract to covert the image and produce the output which is then returned to upload.html and displayed there.

upload.html in the templates file will be used to upload the image and it provides the text converted off of it.

index.html holds the basic page styling

about.html displays the details of the system and the creators of it.

