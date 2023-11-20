# If any number is divisible by 2, and it's remainder is zero then that number will be Even; If it's not then Odd

num1 = int(input("Enter a number to check whether Even or Odd : "))
if num1 % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")