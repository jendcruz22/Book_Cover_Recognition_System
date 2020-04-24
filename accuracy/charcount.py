import string
str1 = input("Please Enter your Own String : ")
str1 = str1.lower().replace(',','').replace('\n',' ').replace('_','').replace(':','').replace('=','').replace('(','').replace(')','').replace('"','').replace('|','').replace('#','').replace('$','').replace('&','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')

print(str1)
total = 0
 
for i in str1:
    total = total + 1
 
print("Total Number of Characters in this String = ", total)
