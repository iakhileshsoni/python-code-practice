# list1 = [10, 12, 15, 20]
#
# # 11, 13,
#
# for i in list1:
#     pass



# Index of Leftmost Repeating Character
# def leftMostRepeatingString(s1):
#     for st in range(len(s1)):
#         for j in range(st+1, len(s1)):
#             if s1[st] == s1[j]:
#                 return st
#     return -1
#
#
# s1 = "adbcdddee"
# print(leftMostRepeatingString(s1))


# Index of leftmost non-repeating character
# def leftmost_non_repeating_char(s1):
#     for i in range(len(s1)):
#         flag = False
#         for j in range(i+1, len(s1)):
#             if i != j and s1[i] == s1[j]:
#                 flag = True
#                 break
#         if not flag:
#             return i
#     return -1
#
#
# s1 = "abbacdee"
# print(leftmost_non_repeating_char(s1))
#
# def leftmost_non_repeating_char(s):
#     for i in range(len(s)):
#         flag = False
#         for j in range(len(s)):
#             if i != j and s[i] == s[j]:
#                 flag = True
#                 break
#         if not flag:
#             return i
#     return -1
#
# # Test the function
# input_str = "abgdbacdcee"
# result = leftmost_non_repeating_char(input_str)
# if result != -1:
#     print(f"The index of the leftmost non-repeating character is {result}")
# else:
#     print("No non-repeating character found.")




# def leftMostNonRepeatingString(s1):
#     char_count = {}
#
#     # First pass: Count the frequency of each character
#     for char in s1:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#
#     # Second pass: Find the leftmost non-repeating character
#     for i, char in enumerate(s1):
#         if char_count[char] == 1:
#             return i
#
#     return -1
#
#
# s1 = "geeksforgeeks"
# print(leftMostNonRepeatingString(s1))


# from abc import ABC, abstractmethod
# class Shape(ABC):  # Define an abstract base class
#     @abstractmethod
#     def area(self):
#         print("Area")
#
#     @abstractmethod
#     def perimeter(self):
#         print("Perimeter")
#
# class Rectangle(Shape):  # Subclass that implements the abstract methods
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
# obj = Rectangle(10, 20)
# print("Area of rectangle is : ", obj.area())








# print 1 to 100
"""
1, 4, 7 ,11

"""

numbers = None
for i in range(1, 101):
    while i==1:
        numbers += 3


# Find the corresponding day of the week for that date. Try to use the above code

from datetime import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int):
        date_obj = datetime(year, month, day)
        day_of_week = date_obj.strftime("%A")
        return day_of_week

day = 30
month = 8
year = 2019

obj = Solution()  # Create an instance of the Solution class
day_of_week = obj.dayOfTheWeek(day, month, year)
print("The day of the given week is:", day_of_week)























"""




customers = 
name
email

products = product_name

orders = 
customer = models.ForeignKey(Customer)
product = models.ForeignKey(Product)




all the customers with their orders and products in the orders


cust = customers.objects.orderset_all()



branchA - 
branchB - 



git pull branchB, 


git merge branchB





"""
