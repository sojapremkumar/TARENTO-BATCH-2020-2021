"""
Question:2

 Accept a String input
- Print the count of words in the String. Space is assumed to be the separator between words
- Print all numbers that are present in the String and also if they are odd or even. Numbers which are together should be counted as one number.
 
"""
 
import re
 
"""
Reading a string from the user.
"""	
str=input("ENTER THE STRING : ")
"""
Calculating the total no.of words in the given string
"""
count=len(str.split())
"""
print the total no.of words
"""
print(" THE COUNT OF WORDS IN THE GIVEN STRING  :: ",count)
"""
finding the even or odd numbers which are present in the given string
"""
e=list()
o=list()
n=re.findall("[0-9]+",str)
n=[int(i) for i in n]
for i in n:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
e=set(e)
o=set(o)
"""
displaying the even and odd numbers
"""
print("ODD NUMBERS PRESENT IN THE GIVEN STRING  ::",end=" ")
print(*o,sep=',')
print("EVEN NUMBERS PRESENT IN THE GIVEN STRING ::",end=" ")
print(*e,sep=',')

