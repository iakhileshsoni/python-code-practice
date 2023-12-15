"""



"""


class Solution:
    def validParentheses(self, s: str) -> bool:   # -> here this sign represents that method will return bool by default
        # Create a pair of opening and closing parenthesis
        opcl = {'(': ')', '[': ']', '{': '}'}  # or  opcl = dict([ ('(', ')'), ('[', ']'), ('{', '}') ])
        # Create stack data structure
        stack = []
        # Traverse each charater in input string
        for i in s:
            # If open parentheses are present, append it to stack
            if i in '([{':
                stack.append(i)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not
            # If not, we need to return false
            elif len(stack) == 0 or i != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not
        # If the stack is empty it means every opened parenthesis is being closed and, we can return true, otherwise we return false
        return len(stack) == 0

obj = Solution()

target = "({)"
result = obj.validParentheses(target)

print(result)