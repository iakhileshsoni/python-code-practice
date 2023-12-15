"""

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]

        return ans

obj = Solution()

string = ["flower","flow","flight"]

result = obj.longestCommonPrefix(string)

print("The Longest common prefix is : ", result)

