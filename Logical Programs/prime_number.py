# Generate n Prime Numbers

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