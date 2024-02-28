import re

#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
inp = str(input())
check = re.compile('a[b]*') 
n = check.search(inp)
print(n)

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
inp = str(input())
check = re.compile('ab{3}|ab{2}')
n = check.search(inp)
print(n)

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.
inp = str(input())
check = re.compile('^[a-z]+_[a-z]+$')
n = check.search(inp)
print(n)

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
inp = str(input())
check = re.compile('[A-Z][a-z]+')
n = check.search(inp)
print(n)

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
inp = str(input())
check = re.compile('a.*?b$')
n = check.search(inp)
print(n)

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
inp = str(input())
check = re.sub("[ ,.]", ":", inp)
print(check)

#7 Write a python program to convert snake case string to camel case string.
s = str(input())
words = s.split('_')
camel = words[0] + ''.join(word.capitalize() for word in words[1:])
print(camel)

#8 Write a Python program to split a string at uppercase letters.
inp = str(input())
check = re.findall("[A-Z][^A-Z]*", inp)
print(check)

#9 Write a Python program to insert spaces between words starting with capital letters.
inp = str(input())
check = re.findall("[A-Z][^A-Z]*", inp)
print(*check)

#10 Write a Python program to convert a given camel case string to snake case.
inp = str(input())
check = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', inp)
n = re.sub('([a-z0-9])([A-Z])', r'\1_\2', check).lower()
print(n)


