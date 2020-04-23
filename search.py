# importing csv module 
import csv 
  
# csv file name 
tesscsv = "tess.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 

text="ONE WORD BUT MANY TONGUES CONFESSIONS OF A MULTICULTURALIS: MATTHEW J, MOTYKA".lower().replace(',','').replace(' ','').replace('_','').replace(':','').replace('=','').replace('(','').replace(')','').replace('"','').replace('|','').replace('#','').replace('$','').replace('&','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')

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
            print("Author: "+row[2]