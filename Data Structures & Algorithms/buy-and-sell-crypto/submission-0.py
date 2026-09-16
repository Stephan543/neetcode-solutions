class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        n = len(prices)
        for i in range(n):

            for j in range(i, n):
                res = prices[j] - prices[i]
                maxP = max(res, maxP)

        return maxP