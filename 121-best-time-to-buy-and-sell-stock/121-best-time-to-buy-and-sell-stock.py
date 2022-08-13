class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        loc, tot = 0, 0
        for i in range(len(prices)-1):
            loc = max(0, loc + prices[i+1] - prices[i])
            tot = max(loc, tot)
        return tot