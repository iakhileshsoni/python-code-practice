# Roman to Int

class Solution:
    def romanToInt(self, s: str):
        roman_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0

        for i in range(len(s)):
            if i > 0 and roman_list[s[i]] > roman_list[s[i - 1]]:
                num += roman_list[s[i]] - 2 * roman_list[s[i - 1]]
            else:
                num += roman_list[s[i]]

        return num

obj = Solution()

roman_num = 'XI'
result = obj.romanToInt(roman_num)

print("Integer of given Roman : {}".format(roman_num), "is {}".format(result))
