# 1. Check if given string is palindrome
def isPalindrome(s):
    return s == s[::-1]

s = "akhil"
ans = isPalindrome(s)
if ans:
    print("Yes, It is Palindrome", "\n")
else:
    print("No, It's not a palindrome", "\n")