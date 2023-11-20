"""
Here I'll put all the definitions and functions with examples
String Programs by GFG:     https://www.geeksforgeeks.org/python-string-exercise/
"""

"""
String : 

A string is a data structure in Python that represents a sequence of characters. There is no concept of Character data types in Python, 
so any Single or group of character withing Single or Double quote is considered as a String

"""

name = '''Akhilesh'''

print(type(name)) # <class 'str'>


# To check the length of a string
print(len(name)) # 8


# To check if specified character is present in string. If not then use 'not in'
print("hi" in name) # True


# Slicing the string - [start index : end index : ]
print(name[1:8]) # khilesh


# Escape Sequencing of a string
String1 = "Hello, I\'m a Geek"
print("Escaped String: ")
print(String1, "\n")  # Hello, I\'m a Geek


# Slicing of string
b = "Hello, World!"
print(b[:5], "\n") # Hello





""" ************************************************* Interview Questions on String ************************************************* """

# 1. Split a string
'''
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax
string.split(separator, maxsplit)
'''

str = "Akhilesh, Kumar Soni"
print(str.split(", "))   # ['Akhilesh', 'Kumar Soni']

str2 = "hello, my name is Peter, I am 26 years old"
print(str2.split(" ", 1), "\n")


