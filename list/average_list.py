# 1. Average of List

# using built-in function

l1 = [10, 20, 30, 40]
avg = sum(l1)/len(l1)
print("Average of list is : ", avg)


# without built-in function
def Average(l1):
    sum = 0
    for i in l1:
        sum = sum + i
    num = len(l1)
    return sum/num

l1 = [10, 20, 30, 40]
print("Average of the given list is : ", Average(l1))