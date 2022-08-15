class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        res = [0] * (n+1)
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2,n):
            res[i] = min(res[i-1], res[i-2]) + cost[i]
        res[n] = min(res[n-2], res[n-1]) 
        print(res)
        return res[n]  