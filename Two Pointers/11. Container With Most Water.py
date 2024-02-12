class Solution:
    def maxArea(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) -1
        width = len(nums) -1
        res = 0
        while left < right:
            if nums[left] < nums[right]:
                height = nums[left]
                left += 1
            else:
                height = nums[right]
                right -= 1
            area = height * width
            width -= 1
            res = max(area,res)
        return res
obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))

