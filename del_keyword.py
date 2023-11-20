# del keyword

"""  del is a keyword which is used to delete the variable/object from the memory  """

"""

1. del vs multiple variable

x = 10
del x

if we no longer require to use x variable then we should delete this variable because this object will be there in the 
memory so unnecessary memory will be wasted.

Once we use del keyword, Garbage collector will destroy this object from the memory and free the memory. Also Chance of 
failing the program with memory will be very less.

Once we use del then we can't access x cuz it's deleted permanently and NameError will be there

"""


# x = 10
# print(x)
# del x
# print(x)


"""
x = 10
y = x
z = y

There is only one object 10 but 3 reference variables x, y, z. If we delete x then only x will be deleted but
y and z will still be pointing to 10 and we can access using y and z.

"""

x = 10
y = x
z = y
print("X before deleting is : ", x)
del x
print("Y is : ", y)
print("Z is : ", z)
print("\n")



"""  
2. del with immutable - 
We can delete reference variable which is pointing the immutable object because we're not performing any changes on that.

s1 = "Akhilesh"
del s1

But we can't change the element of immutable object. Like
del s1[1] - Error
"""

# s1 = "Akhilesh"
# del s1
# del s1[1]
# print(s1)   #  TypeError: 'str' object doesn't support item deletion



"""
3. del with None - 

We can't use variable after del like a = 10; del a; print(a) is error. But after assigning with None we can access that variable. 

"""


a = 10
# del a
a = None
print("a is: ", a)





