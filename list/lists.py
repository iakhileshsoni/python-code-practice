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