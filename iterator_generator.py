'''

An iterator is an object that contains a countable number of values. It consists of the methods  __iter__()  and  __next__()

Iterator vs Iterable:
Lists, tuples, dictionaries, and sets are all Iterable Objects. They are iterable 'containers' from which we can get an iterator.

All these objects have a iter() method which is used to get an iterator:

To prevent the iteration to go on forever, we can use the  StopIteration  statement
'''

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))       # apple     -->  The next() function returns the next item in an iterator.
print(next(myit))       # banana


"""  

Generator in Python

In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

Create Python Generator:
In Python, similar to defining a normal function, we can define a generator function using the def keyword, but instead of the return statement 
we use the yield statement.

def generator_name(arg):
    # statements
    yield something



"""


def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

for value in my_generator(3):
    # print each value produced by generator
    print(value, end=" ")  #  0 1 2


