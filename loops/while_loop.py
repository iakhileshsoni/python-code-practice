# pring numbers from 1 to 10
i = 1
while i<=10:
    print(i)
    i += 1
print("\n")


# pring Hello Guys 4 times
i = 1
while i<5:
    print("Hello Guys")
    i += 1
print("\n")


# print the numbers from 1 to 20 which are divisible by 3
i = 1
while i <=20:
    if i%3 == 0:
        print(i)
    i += 1

# iterate the loop until enter the correct name

name = ''
while name != 'Sunny':
    name = input("Enter your favourite Actress : ")  # it will ask to enter the name until We enter Sunny
print("Thanks for confirming")



# If we want to execute loop infinite time
i = 1
while True:
    print("Hello, ", i)
    i += 1