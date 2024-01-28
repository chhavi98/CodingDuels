class Solution:
    def maxProfit(self, arr: list[int]) -> int:
        s = 0
        for i in range(1, len(arr)):
            p = arr[i] - arr[i-1]
            if p > 0:
                s = s+p
        return s
obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))