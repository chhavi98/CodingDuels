class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        hmap = {}
        indx = 0
        for n in nums:
            count = hmap.get(n, 0)
            if count < 2:
                nums[indx] = n
                hmap[n] = hmap.get(n, 0) + 1
                indx += 1
        print(nums)
        return indx
obj = Solution()
print(obj.removeDuplicates([1,1,1,2,2,3]))