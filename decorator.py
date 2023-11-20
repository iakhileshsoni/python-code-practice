
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
