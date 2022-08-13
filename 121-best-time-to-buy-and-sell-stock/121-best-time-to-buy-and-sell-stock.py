class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small, big = prices[0], prices[0]
        diff = 0
        for i in range(1,len(prices)):
            if prices[i] > big:
                big = prices[i]
                if (big - small) > diff:
                    diff = big - small
            if prices[i] < small:
                small = prices[i]
                big = prices[i]
            print(big, small)
        return diff