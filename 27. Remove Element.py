class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        print(nums)

obj = Solution()
obj.removeElement([3,2,2,3],3)