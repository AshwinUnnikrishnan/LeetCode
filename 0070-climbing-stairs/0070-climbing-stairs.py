class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2]:
            return n
        #Base Case
            # To reach 1st I can do it in 1 way and to reach second in 2 ways (11,2)
        res = [0 for i in range(n)]
        res[0] = 1
        res[1] = 2
        for i in range(2,n):
            res[i] = res[i-1] + res [i-2]
        return res[n-1]