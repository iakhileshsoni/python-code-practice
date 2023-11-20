"""
Largest element in the list

Simple method : for every element check if it is the largest

"""
def LargestElement(l1):
    for i in l1:
        for j in l1:
            if j > i:   # if second value is greater than first then break
                break
        else:
            return i
    return None     # in case of empty list it will return None value

l1 = [10, 20, 15, 31, 30, 40]
print("Largest elemlent of the list using nested loop is : ", LargestElement(l1))


# linear

def LargestElement(l1):
    if not l1:
        return None
    else:
        largest = l1[0]
        for i in range(1, len(l1)):
            if l1[i] > largest:
                largest = l1[i]
        return largest

l1 = [10, 20, 15, 31, 30, 40]
print("Largest element of the list with single loop is : ", LargestElement(l1))





# Second-largest number in the list

def SecondLargest(l1):
    first_largest = float('-inf')
    second_largest = float('-inf')
    for num in l1:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    return second_largest

l1 = [10, 20, 15, 31, 30, 40]
# second_largest = SecondLargest(l1)
print("Second Largest element of the list is : ",SecondLargest(l1))
print("\n")