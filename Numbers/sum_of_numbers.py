# using list - also take input dynamically

# list1 = eval(input("Enter a list of numbers"))  # eval function is used to take input as a list
# # using in-built function - sum()
# print(sum(list1))


# another way

# sum = 0
# for x in list1:
#     sum = sum + x
# print("Sum of given number is : ", sum)


# Sum of first n numbers

n = int(input("Enter a number"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print("Sum of first n number is : ", sum)
