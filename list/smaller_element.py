# Get smaller element in the list
def GetSmall(l1):
    smaller = []
    # num = int(input("Enter a number to find smaller values : "))
    num = 31
    for i in l1:
        if i < num:
            smaller.append(i)
    return smaller

l1 = [10, 20, 15, 31, 30, 40]
smaller_val = GetSmall(l1)
print("Smaller values are : ", smaller_val)