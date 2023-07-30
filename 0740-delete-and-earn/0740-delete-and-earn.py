class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        max_value = max(nums)
        sub_array = (max_value+1) * [0]

        for val in nums:
            sub_array[val] += val
        
        dp = [0] * (max_value + 1)
        dp[1] = sub_array[1]
        
        for i in range(2, max_value + 1):
            # Either consider the current number or skip it
            dp[i] = max(dp[i - 1], dp[i - 2] + sub_array[i])
        
        return dp[max_value]