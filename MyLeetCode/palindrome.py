# Palindrome Number

class Palindrome:
    def isPalindrome(self, num):
        x = str(num)
        reversed_num = x[::-1]
        if x == reversed_num:
            return True
        else:
            return False

obj = Palindrome()

num = 121
result = obj.isPalindrome(num)

print("Given number {0} ".format(num) + " is Palindrome")
