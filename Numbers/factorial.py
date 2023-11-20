""" Find the factorial of given number """

"""
The factorial of a number is the product of all the integers from 1 to that number. For ex Factorial of 4 is 4*3*2*1 = 24
"""

# num = int(input("Enter a number to get the factorial : "))

# factorial = 1
#
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial*i
#     print("The factorial of",num,"is",factorial)


def factorial(x): # 5,4,3,2,1
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

num = int(input("Enter a number to get the factorial : "))  # 5

result = factorial(num)
print("The factorial of", num, "is", result)
