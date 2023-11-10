class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        hashM = {}
        
        
        n = len(nums)
        if n < 2:
            return False
        
        hashM[0] = -1
        sumV = 0
        for i, n in enumerate(nums):
            sumV += n
            r = sumV%k
            if r not in hashM:
                hashM[r] = i
            elif i - hashM[r] > 1:
                return True
        return False