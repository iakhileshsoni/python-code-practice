# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
# A number that can be divided exactly only by itself and 1, for example 7, 17 and 41

# Method - 1  Using Flag variable

# num = 11
#
# def PrimeNumber(num):
#     flag = False
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 flag =  True
#                 break
#         if flag:
#             print("Given number {} is not a prime number".format(num))
#         else:
#             print("Given number {} is a prime number".format(num))
#
# PrimeNumber(num)



# Method - 2 Using for...else loop


num = 39

def PrimeNumber(num):
    if num == 1:
        print("Given number {} is not a prime number".format(num))
    elif num>1:
        for i in range(2, num):
            if (num%i) == 0:
                print("Given number {} is not a prime number".format(num))
                break
        else:
            print("Given number {} is a prime number".format(num))
    # If given input is less than or equal to 1, it is not a Prime Number.
    else:
        print("Given number {} is not a prime number".format(num))
PrimeNumber(num)
