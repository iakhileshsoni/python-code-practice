"""
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation  Fn = Fn-1 + Fn-2
0, 1, 1, 2, 3, 4, 5, 8, 13, 21

"""
def fibonacci(n):
    a = 0
    b = 1
    print(a)
    while b < n:
        print(b)
        a, b = b, a + b   # swap the variable

fibonacci(6)


# using for loop
def fibonacci2(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)

fibonacci2(6)


