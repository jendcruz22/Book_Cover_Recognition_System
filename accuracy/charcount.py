import string
str1 = input("Please Enter your Own String : ")
str1 = str1.lower().replace(' ','')
print(str1)
total = 0
 
for i in str1:
    total = total + 1
 
print("Total Number of Characters in this String = ", total)
