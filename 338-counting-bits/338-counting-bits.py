class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0] * (n+1)
        res[1] = 1
        count = 1
        j = 0
        powCount = 2
        for i in range(2, n+1):
            res[i] = count + res[j]
            j += 1
            if (i+1) == pow(2,powCount):
                powCount += 1
                j = 0
        #print(res)
        return res