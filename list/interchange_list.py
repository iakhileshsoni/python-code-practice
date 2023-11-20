
"""   Python program to swap/interchange first and last elements in a list   """

# Approach-1 : using comma function
def swapList(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1

newList = [23, 65, 19, 90]
print("After swapped first and last element : ", swapList(newList))

