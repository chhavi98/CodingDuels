class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit,profit)
            minPrice = min(prices[i], minPrice)
        return maxProfit
obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))