# Using for loop

def fact(num):
    ans = 1
    if num < 0:
        print("Sorry factorial of negative number doesn't exist")
    elif num == 0:
        print("Factorial of zero is 1")
    else:
        for i in range(1, num+1):
            ans = ans * i
        return ans
print(fact(4))

