"""
Here I'll put all the definitions and functions with examples
Tuple Programs by GFG:    https://www.geeksforgeeks.org/python-tuple-exercise/
"""

"""

Tuples are -->   Ordered  =  Immutable/unchangeable  =  duplicate members  =  indexed

Tuple is faster than the list because of static in nature.

tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry"))


"""


# Count the elements present in the tuples
tuple1 = ("a", "b" , "c" , "c")
print(tuple1.count("c"))


# check how many items a tuple has
tuple1 = ("a", "b" , "c" , "c")
print("Total items in tuple1 are : ", len(tuple1))


# Join 2 tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print("After joining the tuples : ", tuple3)


# # Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print("After Multiplying the tuples : ", mytuple)


# Indexing in Tuple

tuple1 = ("a", "b" , "c" , "c")
print(tuple1[3])   # will throw an error as IndexError: tuple index out of range


# Changing the Tuple values
x = ("apple", "banana", "cherry")
y = list(x)
print("Tuple after converting in List : ", y)
y[1] = "kiwi"
x = tuple(y)

print("Tuple after updating the List and converting again in the Tuple : ",x)



# Add Items into a tuple


# 1. Convert into a list:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)  # O/P  -->   ('apple', 'banana', 'cherry', 'orange')

# 2. Add tuple to a tuple.
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)   # O/P  -->   ('apple', 'banana', 'cherry', 'orange')


# Remove Items from a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)   # O/P   -->  ('banana', 'cherry')


# The  del  keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)   #  this will raise an error because the tuple no longer exists



# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

'''
apple
banana
cherry
'''




