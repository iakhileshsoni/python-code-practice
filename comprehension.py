
"""******************************************      List comprehension      ******************************************"""

'''
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
List Comprehension allows us to create a list using for loop with lesser code. We cannot use while in a list comprehension.
'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [i for i in fruits if "a" in i]
print("List comprehension result : ", new_list)


list = [i for i in range(11) if i % 2 == 0]
print(list)     # [0, 2, 4, 6, 8, 10]




'''******************************************  Tuple comprehension is not supported  ******************************************'''




"""**********************************************      Generator Expressions      ********************************************"""

'''
Generator Expressions are somewhat similar to list comprehensions, but Generator doesn’t construct list object. 
Instead of creating a list and keeping the whole sequence in the memory, the generator generates the next element in demand.

When a normal function with a return statement is called, it terminates whenever it gets a return statement. But a function with a yield 
statement saves the state of the function and can be picked up from the same state, next time the function is called.

The Generator Expression allows us to create a generator without the yield keyword.
'''

generator_expression = (i for i in range(11) if i % 2 == 0)

print(generator_expression)     # <generator object  at 0x000001452B1EEC50>

'''  In the above example, if we want to print the output for generator expressions, We can simply iterate it over generator object.  '''

for i in generator_expression:
    print(i, end=" ")       # 0 2 4 6 8 10
    print("\n")


"""  Check whether Generator Expressions are Time Efficient too as ther're Memory Efficient  """

#List Comprehension:
import timeit
print(timeit.timeit('''list_com = [i for i in range(100) if i % 2 == 0]''', number=1000000))    # 3.341416199997184

#Generator Expression:
import timeit
print(timeit.timeit('''gen_exp = (i for i in range(100) if i % 2 == 0)''', number=1000000))     # 0.3297195000050124






"""*********************************************      Set Comprehension      *********************************************"""
'''
Set comprehension is written within curly braces{}.Returns new set based on existing iterables. 
'''

s1 = {n for n in range(1, 11) if n % 2 == 0}
print(s1)   # Output:{2, 4, 6, 8, 10}





"""******************************************      Dictionary Comprehension      ******************************************"""
'''
A dict comprehension needs two expressions separated with a colon followed by the usual “for” and “if” clauses. 
When the comprehension is run, the resulting key and value elements are inserted in the new dictionary in the order they are produced.

Syntax :  {key:value for (key,value) in iterable if conditional}
'''

d1 = {n : n * n for n in range(1, 11)}
print (d1)      #   Output:     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}




