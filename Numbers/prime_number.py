# The positive integer or number greater than 1 and has only 2 factors. It is divisible by 1 and number itself is called Prime number.


# WAP to check whether given number is Prime or not

num = int(input("Enter a number to check whether it's Prime or not : "))   # 5

if num <= 1:
    print("It is not a Prime number")
else:
    is_prime = True
    for i in range(2, num):  # 2, 3, 4    # num//2+1 for better performance
        if num % i == 0:   # 5%2, 5%3, 5%4 will always be False, so it will go out of loop
            is_prime = False
            break
    if is_prime == True:  # Still is_prime is True and this statement will be executed
        print("Number is Prime")
    else:
        print("Number is not a Prime")




# WAP to generate Prime numbers which are less than or equal to given number

num = int(input("Enter a number : "))
n1 = 2
while n1 <= num:
    is_prime = True
    for i in range(2, n1//2+1):
        if n1 % i == 0:
            is_prime = False
            break
    if is_prime == True:   # or if is_prime because of Bool value
        print(n1)
    n1 += 1



# WAP to print first n Prime numbers

num = int(input("Enter a number : "))
count = 0
n1 = 2
while True:
    is_prime = True
    for i in range(2, n1//2+1):
        if n1 % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(n1)
        count += 1
    if count == num:
        break
    n1 += 1



# Using 2 functions

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primeGeneratot(n):
    num = 2
    while n:
        if isPrime(num):
            yield num
            n -= 1
        num += 1
    return

a = primeGeneratot(12)
for i in a:
    print(i, end=" ")