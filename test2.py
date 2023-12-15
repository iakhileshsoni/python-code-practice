list_comprehension = [i for i in range(11) if i % 2 == 0]

print(list_comprehension)


generator_expression = (i for i in range(11) if i % 2 == 0)

print(generator_expression)     # <generator object  at 0x000001452B1EEC50>

# l1 = []
for i in generator_expression:
    # l1.append()
    print(i, end=" ")   # print(l1, end=" ")





# Even or Odd
def EvenOdd(n):
    if n%2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

n = int(input("Enter a number to check whether Even or Odd : "))
EvenOdd(n)


# Leap year check
def LeapYear(n):
    if (n%4 == 0 and n%100 != 0) or (n%400 == 0):
        print("Provided year is Leap Year")
    else:
        print("This is not a leap year")

year = int(input("Enter any year to check whether Leap Year or not : "))
LeapYear(year)


# Digits in a Number

n = int(input("enter a number to find how many digits are there : "))
def CountDigits(n):
    ch = str(n)
    digits = len(ch)
    return digits

total_digits = CountDigits(n)
print(total_digits)


# without built-in function
def CountDigits(num):
    if num == 0:
        return 1
    count = 0
    while num != 0:
        count += 1
        num = num // 10

    return count

num = int(input("enter a number to find how many digits are there : "))
total_digits = CountDigits(num)
print(total_digits)


def get_issuer(card_number):
    issuers = {
        "4": "Visa",
        "5": "MasterCard",
        "37": "American Express",
        "6": "Discover",
    }
    first_digits = card_number[:2]
    issuer = issuers.get(first_digits)

    if issuer:
        return f"The credit card issuer is {issuer}."
    else:
        return "Issuer not recognized."

card_number = input("Enter your credit card number: ")

card_number = ''.join(filter(str.isdigit, card_number))

result = get_issuer(card_number)
print(result)

