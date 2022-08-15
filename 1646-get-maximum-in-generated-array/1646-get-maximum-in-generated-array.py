class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        res = [0] * (n+1)
        res[1] = 1
        final = 1
        for i in range(1,n):
            if (2*i +1) <= n:
                res[2*i] = res[i]
                res[2*i + 1] = res[i] + res[i+1]
                final = max(final, res[2*i], res[2*i+1])
            else:
                break
        print(res)
        return final