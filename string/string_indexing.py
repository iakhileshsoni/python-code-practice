""" Python allows indexing in String just like in list. We can get substring of any string using index """

""" 
Positive index starts from left to right starting from 0 index 
"""

str1 = "Akhilesh"
print(str1[1])      # k


""" 
Negative index starts from right to left starting from -1 index 
"""

str2 = "Akhilesh"
print(str2[-3])     # e


""" 
If we try to access out of index then we immediately will get Index error 
"""

str3 = "Akhilesh"
print(str3[4])     # IndexError: string index out of range



""" 
index():
Python provides index() method to find the index of the first occurrence of an existing 
substring inside a given string. It returns the index of the substring if found, and raises a 
ValueError if the substring is not present.

 
Syntax : 
    string_object.index(substring, start, end)
    
Parameters: 
    1. substring: The string to be searched for.
    2. start (default : 0) : This function specifies the position from where the search has to be started. 
    3. end (default: length of string): This function specifies the position from where the search has to end.

"""

str4 = "Akhilesh"
print(str4.index('hi'))  # 2,  it will return the first position of the substring found
print(str4.index('h', 3))   # 7, it will return the substring 'h' wherever appears after 3rd index


""" 
index() can be used to find the index position of a particular character, or it may be a word. 
"""

str5 = "Geeksforgeeks"
wrd = "geeks"
print("The first position of geeks after 2nd index : ", str5.index(wrd, 2))   # 7, The first position of geeks after 2nd index : 8



""" 
Python String Index() with Start and End Arguments
"""

test_string = "1234gfg4321"

print("finding gfg in string segment 'gfg4' : ", test_string.index('gfg', 4, 8))   # 4

print("finding '21' in string segment 'gfg4321' : ", test_string.index("21", 8, len(test_string)))     # 9

print("finding '32' in string segment 'fg432' using negative index: ", test_string.index("32", 5, -1))   # 8



""" 
using list comprehension 
"""

text = "Hello this is Akhilesh Soni"
substring_list = ['this', 'Akhilesh', 'notfound']
indices = [text.index(sub) if sub in text else -1 for sub in substring_list]
print("Here are all the indices present in text : ", indices)

# same logic using for loop and if statement but without list comprehension

txt = "Hello Geeks and welcome to Geeksforgeeks"
subs_list = ["Geeks", "welcome", "notfound"]

for sub in subs_list:
    if sub in txt:
        print(txt.index(sub))
    else:
        print(-1)







