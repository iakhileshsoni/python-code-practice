"""     List Programs by GFG:      https://www.geeksforgeeks.org/python-list-exercise/     """



"""


Lists are -->   Ordered  =  Mutable / Changeable  =  Duplicate members  =  Indexed

List is slower than the Tuple because of dynamic in nature.

list() Constructor

this_list = list(("apple", "banana", "cherry"))


"""


list1 = [10, 20, 30, 40]
for list1[0] in list1:  # here list1[0] is just a iterator just like we use i, x or any other variable.
    print(list1[0], end="\n")


# Swapping the list elements
def swapList(str1):

    str1[0], str1[-1] = str1[-1], str1[0]
    return str1
str1 = [12, 35, 9, 56, 24]
print(swapList(str1))


#  The list() Constructor
newlist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(newlist)