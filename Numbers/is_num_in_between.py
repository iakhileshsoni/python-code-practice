# To check whether the given number is in between the range or not

num = int(input("Enter a number : "))

if num <= 100 and num >=1:
    print("The num {} is in between 1 and 100".format(num))
else:
    print("The num {} is not in between 1 and 100".format((num)))


# Another way
# num = int(input("Enter a number : "))
# for num in range(1, 101):
#     if num <= 100 and num >=1:
#         print("The num {} is the in between 1 and 100".format(num))
#     else:
#         print("The num {} is not the in between 1 and 100".format((num)))
