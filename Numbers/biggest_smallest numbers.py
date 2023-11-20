# Biggest Number

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))
num3 = int(input("Enter a third number : "))

if num1 > num2 and num1 > num3:
    print("num1 - {} is the biggest number".format(num1))
elif num2 > num3:
    print("num2 - {} is the biggest number".format(num2))
else:
    print("num3 - {} is the biggest number".format(num3))
print(end="\n")


# Smallest number

num4 = int(input("Enter a fourth number : "))
num5 = int(input("Enter a fifth number : "))
num6 = int(input("Enter a sixth number : "))

if num4 < num5 and num4 < num6:
    print("num4 - {} is the smallest number".format(num4))
elif num5 < num6:
    print("num5 - {} is the smallest number".format(num5))
else:
    print("num6 - {} is the smallest number".format(num6))