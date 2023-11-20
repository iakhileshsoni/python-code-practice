"""  Here we'll perform all the operations on string based on the methods  """

"""

String Methods : 

capitalize()	Converts the first character to upper case
casefold()    	Converts string into lower case
count()     	Returns the number of times a specified value occurs in a string
endswith()     	Returns true if the string ends with the specified value
find()     		Searches the string for a specified value and returns the position of where it was found
format()    	Formats specified values in a string
index()   		Searches the string for a specified value and returns the position of where it was found
islower()    	Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isupper()		Returns True if all characters in the string are upper case
len()       	Returns the length of the string. str.len()
lower()		    Converts a string into lower case
lstrip()		Returns a left trim version of the string
replace()		Returns a string where a specified value is replaced with a specified value
rstrip()		Returns a right trim version of the string
split()		    Splits the string at the specified separator, and returns a list
startswith()    Returns True if a string starts with the given prefix otherwise returns False. str.startswith(prefix, start, end)
strip()		    Returns a trimmed version of the string
upper()		    Converts a string into upper case


"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing spaces
        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            length += 1

        return length

obj1 = Solution()
print(obj1.lengthOfLastWord(s='Akhilesh Kumar Soni'))




