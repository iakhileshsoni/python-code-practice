
n = int(input("Enter a digit from 0 to 9 : "))

if n == 0:
    print("Zero")
elif n == 1:
    print("One")
elif n == 2:
    print("Two")
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Five")
elif n == 6:
    print("Six")
elif n == 7:
    print("Seven")
elif n == 8:
    print("Eight")
elif n == 9:
    print("Nine")
else:
    print("Enter a digit from 0 to 9 only")
print(end="\n")


# Second Way

list1 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
n = int(input("Enter a digit from 0 to 9 : "))
print(list1[n])


# Convert a number into words from the range of 0 to 99

words_upto_19 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

words_for_tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

n = int(input("Enter a digit to get its word : "))

output = ''
if n == 0:
    output = "Zero"
elif n <= 19:
    output = words_upto_19[n]
elif n <= 99:
    output = words_for_tens[n // 10] + " " + words_upto_19[n % 10]
else:
    output = "Please enter number from 0 to 99 only"

print(output)
