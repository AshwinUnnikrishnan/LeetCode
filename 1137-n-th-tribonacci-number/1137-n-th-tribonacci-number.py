class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        for i in range(3,n+1):
            t3 = t0 + t1 + t2
            t2, t1, t0 = t3, t2, t1
        return t2
            