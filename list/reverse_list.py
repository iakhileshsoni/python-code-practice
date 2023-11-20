# Using libraries/direct method

l1 = [10, 20, 30, 40, 50]
l1.reverse()        # it will reverse the same list not create a new list
print("Using reverse() : ", l1)


l2 = [10, 20, 30, 40, 50]
newl = list(l2.__reversed__())  # without converting into list <list_reverseiterator object at 0x000001FAAB9D7940>
print("Using reversed() : ", newl)  # will return a new list

# using list slicing
l3 = [10, 20, 30, 40, 50]
print("Using list slicing : ", l3[::-1])


