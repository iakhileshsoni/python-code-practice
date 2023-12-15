# Logical Operators
print("Logical Operators vs Bitwise Operators")
print("\n")

"""
Logical Operators

Operator	Description	                                                Example	
---------------------------------------------------------------------------------------------
and 	    Returns True if both statements are true	                x < 5 and x < 10
or	        Returns True if one of the statements is true	            x < 5 or x < 4
not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)




Bitwise Operators

Operator	    Name	    Description	                                        Example	
---------------------------------------------------------------------------------------------
& 	            AND	        Sets each bit to 1 if both bits are 1	            x & y	    print(6 & 3) # O/P 2
|	            OR	        Sets each bit to 1 if one of two bits is 1	        x | y	    print(6 | 3) # O/P 7
^	            XOR	        Sets each bit to 1 if only one of two bits is 1	    x ^ y	    print(6 ^ 3) # O/P 5
~	            NOT	        Inverts all the bits	                            ~x          print(~3)   # O/P -4 



Note: 
-----
When you use the boolean 'and' operator the second expression is not evaluated when the first is False. 
Similarly 'or' does not evaluate the second argument if the first is True.
But in case of bitwise operators i.e. &, | all the expressions will be evaluated and will set to 1 as per their definitions.

Boolean operators are usually used on boolean values but bitwise operators are usually used on integer values.
Bitwise operations only make sense with integers and any other type will throw an exception. 
The point here is that Python treats False and True as 0 and 1 respectively: 0 == False and 1 == True are both true



AND = The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
OR  = The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
XOR = The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
NOT = The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0)

"""










# 1. Swap two variables without using a temporary variable

# write a program

# a = 10
# b = 20
#
# a, b = b, a
#
# print(a)
# print(b)


# 2. Check if a number is even or odd using bitwise operators.

# num%2 == 0

# num = int(input("Enter a number to check whether even or odd : "))

# if ~ num%2 == 0:
#     print("Odd number")
# else:
#     print("Even")


# 3. Implement a program to find the square root of a number without using the math module.

# num = int(input("Enter a number to check whether even or odd : "))
#
# sqrt = num ** 0.5
#
# print(int(sqrt))


# 4. Write a program to calculate the area of a circle given its radius

# rad = int(input("Enter radius of the circle to find area : "))
#
# area = 22/7 * (rad ** 2)
#
# print(area)


# 5. Implement a simple calculator program that performs addition, subtraction, multiplication, and division.

# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Error: Division by zero"
#
# # Get user input
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))
#
# # Perform calculations based on the operator
# if operator == "+":
#     result = add(num1, num2)
# elif operator == "-":
#     result = subtract(num1, num2)
# elif operator == "*":
#     result = multiply(num1, num2)
# elif operator == "/":
#     result = divide(num1, num2)
# else:
#     result = "Error: Invalid operator"
#
# # Display the result
# print(f"Result: {result}")




# Write a program to check if a year is a leap year

4
# 100 - century year
400


