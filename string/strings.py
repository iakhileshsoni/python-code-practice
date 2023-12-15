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





'''
All string methods return new values. They do not change the original string.
'''


# name = '''Akhilesh'''
#
# print(type(name)) # <class 'str'>
#
#
# # To check the length of a string
# print(len(name)) # 8
#
#
# # To check if specified character is present in string. If not then use 'not in'
# print("hi" in name) # True


# Slicing the string - [start index : end index : ]
# print(name[1:8]) # khilesh
#
#
# # Reversing a string
# print(name[::-1])
#
#
# # Reversing a string using join() and reversed() function
# print("".join(reversed(name)))
#
# print("\n\tthis is the slicing of the string", "\n") #\n - for new line and \t - for new tab
#
#
# # Deleting a whole string using del
# del name
#
#
# # Escape Sequencing of a string
# String1 = "Hello, I\'m a Geek"
# print("Escaped String: ")
# print(String1, "\n")  # Hello, I\'m a Geek
#
#
# # Slicing of string
# b = "Hello, World!"
# print(b[:5], "\n") # Hello





""" ************************************************* Interview Questions on String ************************************************* """


# 1. Check if given string is palindrome
# def isPalindrome(s):
#     return s == s[::-1]
#
# s = "akhil"
# ans = isPalindrome(s)
# if ans:
#     print("Yes, It is Palindrome", "\n")
# else:
#     print("No, It's not a palindrome", "\n")



# 2. Split a string
'''
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

Syntax
string.split(separator, maxsplit)
'''

# str = "Akhilesh, Kumar Soni"
# print(str.split(", "))   # ['Akhilesh', 'Kumar Soni']
#
# str2 = "hello, my name is Peter, I am 26 years old"
# print(str2.split(" ", 1), "\n")
#
#
#
# # Alternate case (UPPER & lower) of String
#
# str = "akhilesh"
# res = ""
# for i in range(len(str)):
#     if not i % 2:      #  if i % 2: aKhIlEsH
#         res = res + str[i].capitalize()
#     else:
#         res = res + str[i].lower()
#
# print("String after alternate case : ", res)   # AkHiLeSh






# expected output { 'a': 5, 'b': 6, 'c': 3,'d': 5 }

# Approach 1
# test_string = "aaabbbcc"
#
# a = test_string.count('a')
# b = test_string.count('b')
# c = test_string.count('c')
#
# string_dict = {"a": a, "b": b, "c": c}
# print(string_dict, '\n')  # {'a': 3, 'b': 3, 'c': 2}
#
#
# # Approach 2
# from collections import Counter
# test_string2 = "Akhilesh"
# collection = Counter(test_string2)
# print(collection)
# # print(type(collection))     # <class 'collections.Counter'>
#
#
# # Approach 3
# import re
# test_string3 = "akhilesh"
# print(len(re.findall('a', test_string3)))




def length_of_longest_substring(s):
    char_index_map = {}
    max_length = start = 0

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

s1 = "aaaabbbbbbbbbbcdefghhhhhhhhhhhhhhhhh"
print(length_of_longest_substring(s1))

