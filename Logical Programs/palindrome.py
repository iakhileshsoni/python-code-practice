"""
Palindrome:
Palindrome String

"""

# Method1: using Split Method or Negative Indexing   ***

def Palindrome(s):
    temp = s[::-1]
    if s == temp:
        print("Yes, this is a Palindrome")
    else:
        print("No, this is not a Palindrome")

s = Palindrome("PRIYA")



# Method2: using indexing and for loop
def Palindrome2(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            return False
    return True

s = "Akhil"
print(Palindrome2(s))



# Method3: Using reversed and Join functions
def Palindrome3(s):
    temp = ''.join(reversed(s))
    if s == temp:
        return True
    else:
        return False

print(Palindrome3("akki"))



# Method4: Using while loop
def Palindrome4(s):
    n = len(s)
    first = 0
    last = n-1
    while first<last:
        if s[first] == s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True

print(Palindrome4("NITIN"))




"""***************************    Palindrome Number    ***************************"""

# Using While loop
def Palindrome5(n):
    temp = n
    rev_num = 0
    while temp > 0:
        digit = temp % 10
        # print(digit)
        rev_num = rev_num * 10 + digit
        temp = temp // 10
    if n == rev_num:
        return True
    else:
        return False

n = 12321
print(Palindrome5(n))
