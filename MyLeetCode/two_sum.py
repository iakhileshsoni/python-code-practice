# Two Sum

class TwoSum:
    def CheckTwoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

obj = TwoSum()
num_list = [10, 20, 30]
target_value = 40
result = obj.CheckTwoSum(num_list, target_value)
print("The indices of two numbers that add up to target are : ", result)

