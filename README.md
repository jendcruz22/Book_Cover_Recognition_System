# Book Recognition System

[pyt.py](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/pyt.py) is the main file which integrates [ocr_core.py](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/ocr_core.py), [upload.html](), [index.html](), [about.html](). 

[ocr_core.py](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/ocr_core.py) takes the image uploaded in [upload.html](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/templates/upload.html) by the user and uses pytesseract to covert the image and produce an output which may not be accurate. So it is compared with the data in [tess.csv](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/tess.csv) and the appropriate Name of the book and its author is then returned to upload.html and displayed there.

[upload.html](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/templates/upload.html) will be used to upload the image and it prints the text converted off of the entered image for the user.

[index.html](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/templates/index.html) holds the basic page styling

[about.html](https://github.com/jendcruz22/Book_Cover_Recognition_System/blob/master/templates/about.html) displays the details of the system and the creators of it.

