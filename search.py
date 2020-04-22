
# importing csv module 
import csv 
  
# csv file name 
tesscsv = "tess.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 

text="Sophia Meas"

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
        if col == text:
            print("Name of the book: "+row[1]) 
            print("Author: "+row[2])
        
