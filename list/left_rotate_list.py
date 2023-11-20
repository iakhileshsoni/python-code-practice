# Write a program to left rotate a list by 1. For ex. 1st element will shift in the last, 2nd will shift in 1st etc...

# using list slicing
def LeftRotateList(l1):
    res = l1[1:] + l1[0:1]
    return res

l1 = [10, 20, 30, 40]
print("Using list slicing : ", LeftRotateList(l1))
print('\n')


# using pop() and append() function
def LeftRotateList(l1):
    l1.append(l1.pop(0))    # pop first element and then append will add element in the last
    return l1

l1 = [10, 20, 30, 40]
print("Using append and pop function : ", LeftRotateList(l1))
print('\n')



# using our own logic   -   one traversal and no need any auxiliary space
def LeftRotateList(l1):
    n = len(l1)
    i = l1[0]
    for x in range(1, n):
        l1[x-1] = l1[x]
    l1[n-1] = i

    return l1

l1 = [10, 20, 30, 40]
print("Using own logic : ", LeftRotateList(l1))
print('\n')

# LeftRotateList(l1)
# print(l1) # If we don't return l1 inside function then can use these 2 commented lines


