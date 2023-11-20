# check if list is sorted
def isSorted(l1):
    for i in range(1, len(l1)):
        if l1[i] < l1[i-1]:
            return False
    return True

# l1 = [10, 50, 15, 31, 30]
l1 = [10, 20, 30, 40, 11]
if isSorted(l1):
    print("List is sorted!")
else:
    print("List is not sorted!!")




