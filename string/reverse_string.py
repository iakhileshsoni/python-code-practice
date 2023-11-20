""" All string methods return new values. They do not change the original string. """

original_string = "akhil"

reversed_string = ''.join(reversed(original_string))
print(reversed_string)


"""
Why we need join?

When you use the reversed() function on a string, it returns a reverse iterator, not a reversed string.
This iterator can be used to iterate over the characters of the string in reverse order. To obtain the reversed string, 
you need to convert the iterator back into a string using the str.join() method or another method that combines the characters.
"""



"""  WAP to reverse the order of words in given string  """

s = 'Hello Guys how are you doing'
word = s.split(" ")     # split - splits the string based on the seperator
new = word[::-1]
new_word = " ".join(new)    # join -  join combines list elements based on the seperator
print(new_word, end=" ")



"""  WAP to reverse the internal content of words in given string not reverse a word """

print("Original string is : ", s)
word = s.split()
new_content = ''
for i in word:
    content = i[::-1]
    # new_content = ''.join(content)
    print(content, end=" ")




""" WAP to reverse a String in different ways  """

# 1. using slice operator

s = input("Enter some string to reverse : ")
print("The reversed string is : ", s[::-1])  # Slice operator step value can't be zero (0). If we don't specify begin and end value then whole string will be considered


# 2. Using in-built reversed function
s = input("Enter some string to reverse : ")
ns = reversed(s)
output = ''.join(ns)
print("The reversed string is : ", output)

# Or

print("".join(reversed(s)))

print("\n\tthis is the slicing of the string", "\n") #\n - for new line and \t - for new tab


# 3. Using while loop without any in-built function except len()
s = input("Enter some string to reverse : ")
output = ''
i = len(s)-1
while i>=0:
    output = output + s[i]
    i = i -1
print(output)




