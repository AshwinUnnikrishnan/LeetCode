class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        max_value = dp[0]
        
        for i in range(1,n):
            
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
            if dp[i] > max_value:
                max_value = dp[i]
        return max_value