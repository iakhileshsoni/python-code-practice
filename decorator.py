'''
A decorator is a design pattern that allows us to modify the functionality of a function or class by wrapping it in another function
'''
def decorator_func(func):
    def wrapper_func():
        print("Hello Wrapper Function")
        return func()
    print("Hello Decorator Function")
    return wrapper_func

def show():
    print("Hello Show Function", "\n")
decorator_show = decorator_func(show)
decorator_show()


#************************************    ALTERNATIVE WAY OF WRITING THE DECORATOR FUNCTION    **********************************************#

def decorator_func(func):
    def wrapper_func():
        print("Hello Wrapper Function")
        return func()
    print("Hello Decorator Function")
    return wrapper_func

@decorator_func
def display():
    print("Hello Display", "\n")
display()




# *************************************************************************************************************************#
                            # Create a decorator function to get UPPERCASE string #
# *************************************************************************************************************************#

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi(), "\n")



#*************************************************************************************************************************#
                                    # 2. Using multiple decorators  #
#*************************************************************************************************************************#

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi(), "\n")




# *************************************************************************************************************************#
            #  3. Let’s define a decorator that count the time taken by the function for execution.   #
# *************************************************************************************************************************#

import time

def timeis(func):
    ''' Decorator that reports the execution time. '''
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(func.__name__, end - start)
        return result

    return wrap

@timeis
def countdown(n):
    '''Counts down'''
    while n > 0:
        n -= 1

countdown(5)
countdown(1000)


def login(func):
    def inner():
        print("Login first")
        func()
    return inner


@login
def profile():
    print("This is your dashboard")

profile()  # Now it will first go to the login() because of @login decorator then will come to profile()


"""
O/P
Login first
This is your dashboard
"""

# We can call profile() with decorator function login() also like this:

# decorate the ordinary function
decorated_func = login(profile)

# call the decorated function
decorated_func()


"""
Note : Here in this example login() is a decorator
"""
