# Separate even and odd

def EvenOdd(l1):
    even = []
    odd = []
    for i in l1:
        if i%2 ==0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd    # whenever function returns multiple values then it will be Tuple

l1 = [10, 20, 15, 31, 30, 40]
even, odd = EvenOdd(l1) # Unpack the tuple into list

print("Even list is : ", even)
print("Odd list is : ", odd)