from functools import reduce

#1 Write a Python program with builtin function to multiply all the numbers in a list
def multiply(x, y):
    return x * y
def MultiplyList(integ):
    result = reduce(multiply, integ)
    return result

integ = [2, 3, 7 ,11]
result = MultiplyList(integ)
print(result)

#2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
s = input('input some string with upper- and lowercase letters: ') 
def LScounter(s): 
    up = 0 
    low = 0 
    for i in s: 
        if i.islower(): 
            low += 1
        elif i.isupper():
            up += 1  
    print(f'number of uppercase letters: {up}.\nnumber of lowercase letters: {low}')
    return 0
LScounter(s)

#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input("input a string to check: ")
def Palindrome(s):
    return s == s[::-1]

answer = Palindrome(s)
if answer:
    print("Yes")
else:
    print("No")

#4 Write a Python program that invoke square root function after specific milliseconds.
from time import sleep
import math 
def SqRoot(milliseconds, number):
    sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds: {result}")

milliseconds = float(input("Input milliseconds: "))
number = int(input("Input an int to sqr it: "))
SqRoot(milliseconds, number)

#5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
def TrueValue(n):
    return all(n)

my_tuple = (True, True, True)
print(TrueValue(my_tuple))

# my_tuple = (False, False, False)
# print(TrueValue(my_tuple))



