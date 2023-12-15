"""  Do all the operations in Function here  """
"""

When a function is defined inside a class then it is called Method.
The method is accessible to data that is contained within the class
Each object in Python has a unique id. The id() function returns the object’s id.

"""

"""
Generators
Global and local variable
global keyword
First class functions
Decorators 
Decorators with parameter


A function is a set of instructions or group of statement. We define it once and we can use it n number of times.
We get code re-usability.

def Greet():
    body

We have 2 types of functions in Python: In-built functions and User-defined functions



Difference between Method vs Function


If any functions defined inside a Class then such types of functions are called Methods not a Functions. Like
append() it is defined inside the List class so we call it on list object i.e. list.append(), so it is method not
a function.


We can pass some parameters in function and function can also return some values. Function can return any number of 
values simultaneously 

def Calc(a, b):
    sum = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return sum, sub, mult, div    # and we can hold this value by using tuple variable or any other variable

a, b, c, d = Calc(50, 30)  # any other variable
print(a)
print(b)
print(c)
print(d)

t = Calc(50, 30)   # using tuple variable
for x in t:
    print(x)


Even if we're not returning any value then that time also it will return some value and the type of that value is None

def Greet():
    print("Hello")
print(Greet())   # None


Parameters:
    Positional -  We have to maintain the order in which we're passing the values
    Keyword
    Default
    Var length


"""

# Here we defined one time, but we can use the greeting many times that is the use of function

# def Greet(name):
#     print("Hello, ", name)
#
# Greet("Saroj")
# Greet("Akhil")



"""
1. Positional Argument -  Order of argument and number of positional argument must match with the parameter we're passing otherwise will not
get correct result 
"""

# def Calc(a, b):
#     sum = a + b
#     sub = a - b
#     mult = a * b
#     div = a % b
#     return sum, sub, mult, div
#
# a, b, c, d = Calc(50, 30)
# print(a)
# print(b)
# print(c)
# print(d)




"""
2. Keyword Argument - Order of argument is not important, but instead number of argument is important


We can't pass positional argument after keyword argument. Although we can pass positional and keyword argument simultaneously but
can't pass positional after keyword args because positional argument follows keyword argument. 

def Calc(a, b):
    sum = a + b
Calc(50, b=30)  R  --> It is perfectly valid
Calc(b=50, 30)  X  --> positional argument follows keyword argument
Calc(50, a=30)  X  --> Calc() got multiple values for argument a


We can't pass multiple values at a time for a same argument. For ex

def Calc(a, b, c=40, d=50):
    print(a, b, c, d)
    
Calc(10, 20, b=50, c=30)  

# here a, b are positional arguments and we are already passing 10, 20 so b =50 is incorrect.
And it will throw error by saying -> Calc() got multiple values for b

Also we can't pass undefined keyword argument which is not there in function's parameter. For ex. 
Calc(10, 20, b=50, c=30, d=100) --> Calc() got an unexpected keyword argument 'd'


"""

# def Calc(a, b):
#     sum = a + b
#     sub = a - b
#     mult = a * b
#     div = a % b
#     return sum, sub, mult, div
#
# Calc(a=50, b=30)
# Calc(b=50, a=30)



"""
3. Default argument - Default argument always should be in the last

def Greet(name="Guest", msg):  --> non-default argument follows default argument
    pass

def Greet(msg, name="Guest")
    pass

"""



"""
4. Variable length argument - 

"""

# def Sum(a, b):
#     print(a + b)
# Sum(10, 30)
# print(end="\n")

"""

Here if we want to pass 3 or more parameters and are taking only 2 arguments in the function definition then it will 
throw error. Or else we have to create new function as :

def Sum(a, b, c):
    print(a + b + c)
Sum(10, 30, 50)

But to overcome with this problem we can go with Variable length argument like :

def Sum(*a):
    print(a + b + c)
Sum(10, 30, 50)

"""


# def Greet(*a):  # here a is Tuple internally
#     print("Hello Guys, this is variable length argument")
#
# Greet(1)
# Greet(1, 2)
# Greet(1, 2, 30)
# Greet(1, 2, 30, 40)

def Sum(*n):
    result = 0
    for x in n:
        result = result + x
    print(result)
    print("\n")

Sum()  # 0
print("\n")
Sum(10, 20, 30)   # 60


"""

Well, if we are calling positional and var length argument together then it is valid but we always should call positional
argument with keyword argument. Like :

def Sum(*n, name):
    result = 0
    for x in n:
        result = result + x
    print("The sum by ", name, ":", result)

Sum(name="Akhil", 10, 20)
Sum(name="Ravi", 10, 20, 30)


So If we pass normal argument then variable length then there is not a problem : 

def Sum(name, *n):
    result = 0
    for x in n:
        result = result + x
    print("The sum by ", name, ":", result)

Sum(10, 20, name="Akhil")   # it is valid


but after variable length argument if we pass any other argument(positional) then we should provide values as keyword argument

def Sum(*n, name):
    result = 0
    for x in n:
        result = result + x
    print("The sum by ", name, ":", result)

Sum(10, 20, name="Akhil")


Note : 
    *args - We can pass any number of arguments as a values using var args But 
    **kwargs - We can pass any number of keyword arguments also using  **kwargs
    
def Person(**kwargs):       # here the type of kwargs is Dictionary and we can check using print(type(kwargs))
    print(type(kwargs))
    for k, v in kwargs.items:
        print(k, "--" v)

Person(name="Akhil", email="akhil@mail.com", age=25, color="red")
Person(name="Joy", email="joy@mail.com", age=25, color="red", height=5.6, weight=40)

"""



def Person(**kwargs):       # here the type of kwargs is Dictionary, and we can check using print(type(kwargs))
    print("Type of kwargs is : ", type(kwargs))
    for k, v in kwargs.items():
        print(k, "--", v)

Person(name="Akhil", email="akhil@mail.com", age=25, color="red")
Person(name="Joy", email="joy@mail.com", age=25, color="red", height=5.6, weight=40)







"""**********************************************   Anonymous functions   *********************************************"""

"""

Functions which are nameless while defining are called Anonymous functions. Lambda in python is called an anonymous function.
We define anonymous function using lambda keyword. Syntax is -->   lambda input:expression

We define/call anonymous functions for instant use or one time use depending upon the situation. Like if we want to calculate 
the square of 2 numbers and want to use only once in a project then we can define the anonymous function i.e. 

lambda x: x * n 

Although if we want to call it by some name then we can assign it in any name like 

l = lambda x: x * n then we'll call by l(5)

 
"""

# Square of 2 given numbers
# l = lambda x: x * 5
# print(l(3))


# Sum of 2 given numbers
s = lambda a, b: a + b
print("Sum of {} and {} is {} : ".format(10, 20, s(10, 20)))
""" 10 and 20 is the numbers to put in first 2 brackets & s(10, 20) is the lambda function call """

# Find the biggest number in given 2 numbers
b = lambda a, b: a if a>b else b    # Ternary operator
print("The biggest number between {} and {} is {} : ".format(10, 20, b(10, 20)))

""" 
Comprehension concept is applicable only with collections like List, Tuple, Set, Dictionary that's why here
we have used Ternary operators
"""



"""


Endpoints:
    list of all the users
    list articles
    all the article for particular user


"""