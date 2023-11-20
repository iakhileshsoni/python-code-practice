# Python program to interchange first and last elements in a list



# Approach-1 : Direct method using index
def swapList(str1):

    str1[0], str1[-1] = str1[-1], str1[0]
    return str1
str1 = [12, 35, 9, 56, 24]
print(swapList(str1))      # O/P :  [24, 35, 9, 56, 12]


# Approach-2 : using len() function

def swapList(list1):
    # get the length of the list to assign new value at n-1 position
    size = len(list1)
    temp = list1[0]     # store first element in the variable

    list1[0] = list1[size-1]
    list1[size-1] = temp
    return list1

newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# Approach-3 : using inbuilt function list.pop()

def swapList(list2):
    # First pop out the first and last element of the list
    first = list2.pop(0)
    last = list2.pop(-1)
    list2.insert(0, last)    # insert() will add element in the specified index  while  append() will add in the last index
    list2.append(first)

    return list2
newList = [10, 35, 9, 56, 20]
print(swapList(newList))

