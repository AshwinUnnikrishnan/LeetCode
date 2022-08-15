import math
class Solution:
    def divisorGame(self, n: int) -> bool:
        #
        res = [False] * (n+1)
        if n<2:
            return res[n]
        res[2] = True
        for i in range(3,n+1):
            
            for j in range(1,ceil(math.sqrt(i)+1)):
                print(i,j)
                if i%j == 0 and res[i-j] == False:
                    res[i] = True
                    break
        return res[n]
        