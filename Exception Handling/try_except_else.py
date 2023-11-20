"""  Exception Handling in Python  """

'''
Try except
Errors and exceptions
Built-in exceptions

Error in Python can be of two types i.e. Syntax errors and Exceptions.
Errors are the problems in a program due to which the program will stop the execution.
On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program

try     - Statements that can raise exceptions are kept inside the try claus

except  - Statements that handle the exception are written inside except clause

else    - The else block lets you execute code when there is no error. It must be present after all the except clauses.

finally - finally block is always executed after the try and except blocks

'''


a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))
    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))

except:
    print("An error occurred")



'''  A try statement can have more than one except clause  '''


def fun(a):
    if a < 4:
        b = a / (a - 3)     # throws ZeroDivisionError for a = 3
    print("Value of b = ", b)   # throws NameError if a >= 4

try:
    fun(3)
    fun(5)
# note that braces () are necessary here for multiple exceptions

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")




''' ***********************************   try with else statement    *********************************** '''

def test(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

test(2.0, 3.0)
test(3.0, 3.0)







