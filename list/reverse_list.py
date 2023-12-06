# Using libraries/direct method

# l1 = [10, 20, 30, 40, 50]
# l1.reverse()        # it will reverse the same list not create a new list
# print("Using reverse() : ", l1)
#
#
# l2 = [10, 20, 30, 40, 50]
# newl = list(l2.__reversed__())  # without converting into list <list_reverseiterator object at 0x000001FAAB9D7940>
# print("Using reversed() : ", newl)  # will return a new list
#
# # using list slicing
# l3 = [10, 20, 30, 40, 50]
# print("Using list slicing : ", l3[::-1])


# l1 = [10, 20, 30, 40, 50]
# newarr = []
# for i in l1:
#     newarr.append(i[n])

# def some_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# some_func(10, 20, 'foo', foo='bar', bar='100')

# ar = ['a', 'b', 'c']
# a = zip(range(len(ar)), ar)
# a = list(a)
# b = list(enumerate(ar))
# is_equal = (a == b)
# print(is_equal)



import threading
import time

# def thread_function():
#     print('Hi!')
#     time.sleep(2)
#     print('Good bye!')
#
# if __name__ == "__main__":
#     print('start')
#     x = threading.Thread(target=thread_function)
#     x.start()
#     print("Stop")


# def thread_function(a, b):
#     sum_of_square = 0
#     for i in range(a, b):
#         sum_of_square += a * b
#     print(sum_of_square)
#
# if __name__ == "__main__":
#     x = threading.Thread(target=thread_function, args=(1, 10000))
#     x.start()
#     y = threading.Thread(target=thread_function, args=(10000, 20000))
#     y.start()


# returns 'foo' first then 'bar' --> true or false
import asyncio

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def foo():
#     await say_after(2, 'foo')
# async def bar():
#     await say_after(1, 'bar')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([foo(), bar()]))
# loop.close()



# a, b = 10, 0
# try:
#     c = a/b
# except Exception as exc:
#     c = 5
#
# print(c)



# fruits1 = ['apple', 'banana', 'ship', 'orange']
# fruits2 = ['apple', 'banana']
# fruits3 = [fruit for fruit in fruits1 if fruit not in fruits2]
# print(fruits3)


# print(testlist * 2 if testlist = ['abc', 33])