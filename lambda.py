'''
A lambda function is a small anonymous function.
It can take any number of arguments, but can only have one expression.

Syntax:

lambda arguments : expression

a = lambda x : x + 10
print(a(5))   # 15
'''



# P1: add 20 to argument x and return result
a = lambda x : x + 20
print("Lambda function result: ", a(5))


# P2: multiply argument a with b
x = lambda a, b: a * b
print("After multiplying using Lambda: ", x(5, 4))


# P3:  for loop to iterate over a list of numbers and find the square of each number and save it in the list.
l1 = [2, 3, 4, 6]
l2 = []
for i in l1:
    temp = lambda i : i**2  # <class 'function'>
    l2.append(temp(i)) # we use temp(i) to get elements cuz temp will return <class 'function'>
print("Square of all the elements present in l1 : ", l2)


