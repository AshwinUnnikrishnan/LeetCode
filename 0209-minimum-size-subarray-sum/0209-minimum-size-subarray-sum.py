class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 1
        n = len(nums)
        
        sumV = nums[0]
        if sumV >= target:
            return 1
        max_v=0
        
        while j<n:
            sumV += nums[j]
            if sumV >=target:
                if max_v == 0:
                    max_v = j-i+1
                while sumV >=target:
                    max_v = min(j-i+1, max_v)
                    sumV -= nums[i]
                    i += 1
            j += 1
        return max_v
                    
                    
            
            
        