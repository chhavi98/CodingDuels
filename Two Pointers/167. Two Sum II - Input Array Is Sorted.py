class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        nums = {}
        for i in range(len(numbers)):
            if numbers[i] in nums:
                return (nums.get(numbers[i]) + 1, i + 1)
            else:
                dif = target - numbers[i]
                nums[dif] = i
obj = Solution()
res = obj.twoSum([2,7,11,15],9)
print((res))