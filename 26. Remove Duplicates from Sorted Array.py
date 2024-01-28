class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[::] = list(set(nums))
        print(nums)
        return len(nums)
obj = Solution()
print(obj.removeDuplicates([1,1,2]))