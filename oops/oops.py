"""
Object-Oriented Programming in Python
OOPs Program by GFG:    https://www.geeksforgeeks.org/tag/python-oops-programs/
"""

"""
Classes and objects
Class variables or static variables
Inheritance and its types
Class methods vs static methods
"""


# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# emp = Employee("akhilesh", 32)
# print(emp.name)


class Person:
    name = "akhil"
    age = 25

    def info(self):
        print(f"{self.name} is {self.age} years old")

man = Person()
man.info()







