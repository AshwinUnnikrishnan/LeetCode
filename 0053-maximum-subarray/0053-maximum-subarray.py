class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        sumM = dp[0]
        for i in range(1, n):
            sumTerm = 0
            if dp[i-1] > 0:
                sumTerm = dp[i-1]
            dp[i] = nums[i] + sumTerm
            
            sumM = max(sumM, dp[i])
        return sumM
            
            
        
