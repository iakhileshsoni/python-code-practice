"""     List Programs by GFG:      https://www.geeksforgeeks.org/python-list-exercise/     """



"""


Lists are -->   Ordered  =  Mutable / Changeable  =  Duplicate members  =  Indexed

List is slower than the Tuple because of dynamic in nature.

list() Constructor

this_list = list(("apple", "banana", "cherry"))


"""


# list1 = [10, 20, 30, 40]
# for list1[0] in list1:  # here list1[0] is just a iterator just like we use i, x or any other variable.
#     print(list1[0], end="\n")


# Swapping the list elements
# def swapList(str1):
#
#     str1[0], str1[-1] = str1[-1], str1[0]
#     return str1
# str1 = [12, 35, 9, 56, 24]
# print(swapList(str1))
#
#
# #  The list() Constructor
# newlist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(newlist)


# import sys
#
# x = True
# size_of_x = sys.getsizeof(x)
# print("size of x is : ", size_of_x)



# 2 sum array Problem
# https://leetcode.com/problems/two-sum/description/
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

if __name__ == "__main__":
    # Create an object of the Solution class
    solution_obj = Solution()

    # Example input: a list of numbers and a target
    nums = [2, 7, 11, 15]
    target = 9

    # Call the twoSum method and print the result
    result = solution_obj.twoSum(nums, target)
    print("Indices of the two numbers:", result)



#  The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



l1 = [10, 20, 'akhil', 30, 40]
print(l1)
print(end="\n")

l1.append(50)
print(l1)
print(end="\n")

l1.insert(1, 15)
print(l1)
print(end="\n")


print(l1)
print(end="\n")


l2 = [10, 30, 20, 15]
print("Max is : ", max(l2))
print(end="\n")

print("Min is : ", min(l2))
print(end="\n")

l2.sort()
print("Sorted list is : ", l2)
print(end="\n")

l3 = ['raj', 'Raj', 'akhil', 'nikhil']
l3.sort()
print(l3)
print(end="\n")


l4 = [10, 20, 30, 40, 20, 30]
l4.remove(30)
print("after removing element : ", l4)
print(end="\n")


l5 = [10, 20, 30, 40, 30, 20, 50, 100]
print("after pop method : ", l5.pop())  # pop funtion returns the removed element
print(l5, end="\n")     # o/p  [10, 20, 30, 40, 30, 20, 50]
print(end="\n")


List1 = [10, 20, 30, 40, 50]
del List1[1: 3]
print("after del : ", List1)
print(end="\n")


List1 = [10, 20, 30, 40, 50]
print("Max element of the list is :", max(List1))
print(end="\n")

print("Min element of the list is :", min(List1))
print(end="\n")

List1 = [10, 20, 30, 40, 50]
List1.reverse()
print("Reversed list is :", List1)
print(end="\n")


List1 = [10, 40, 20, 30, 50]
print("Original list is :", List1)
List1.sort()
print("Sorted list is :", List1)
print(end="\n")


List1 = [10, 40, 20, 30, 50]
print("Number of elements present in list are :", len(List1))








"""************************************************ some useful program practice in list ************************************************"""


# 1. Average of List

# using built-in function

l1 = [10, 20, 30, 40]
avg = sum(l1)/len(l1)
print("Average of list is : ", avg)


# without built-in function
def Average(l1):
    sum = 0
    for i in l1:
        sum = sum + i
    num = len(l1)
    return sum/num

l1 = [10, 20, 30, 40]
print("Average of the given list is : ", Average(l1))


# Separate even and odd

def EvenOdd(l1):
    even = []
    odd = []
    for i in l1:
        if i%2 ==0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd    # whenever function returns multiple values then it will be Tuple

l1 = [10, 20, 15, 31, 30, 40]
even, odd = EvenOdd(l1) # Unpack the tuple into list

print("Even list is : ", even)
print("Odd list is : ", odd)



# Get smaller element in the list
def GetSmall(l1):
    smaller = []
    # num = int(input("Enter a number to find smaller values : "))
    num = 31
    for i in l1:
        if i < num:
            smaller.append(i)
    return smaller

l1 = [10, 20, 15, 31, 30, 40]
smaller_val = GetSmall(l1)
print("Smaller values are : ", smaller_val)



""" 
Largest element in the list

Simple method : for every element check if it is the largest

"""
def LargestElement(l1):
    for i in l1:
        for j in l1:
            if j > i:   # if second value is greater than first then break
                break
        else:
            return i
    return None     # in case of empty list it will return None value


l1 = [10, 20, 15, 31, 30, 40]
print("Largest elemlent of the list using nested loop is : ", LargestElement(l1))



# linear

def LargestElement(l1):
    if not l1:
        return None
    else:
        largest = l1[0]
        for i in range(1, len(l1)):
            if l1[i] > largest:
                largest = l1[i]
        return largest

l1 = [10, 20, 15, 31, 30, 40]
print("Largest element of the list with single loop is : ", LargestElement(l1))


# Second-largest number in the list

def SecondLargest(l1):
    first_largest = float('-inf')
    second_largest = float('-inf')
    for num in l1:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    return second_largest

l1 = [10, 20, 15, 31, 30, 40]
# second_largest = SecondLargest(l1)
print("Second Largest element of the list is : ",SecondLargest(l1))
print("\n")


# check if list is sorted
def isSorted(l1):
    for i in range(1, len(l1)):
        if l1[i] < l1[i-1]:
            return False
    return True

# l1 = [10, 50, 15, 31, 30]
l1 = [10, 20, 30, 40, 11]
if isSorted(l1):
    print("List is sorted!")
else:
    print("List is not sorted!!")
