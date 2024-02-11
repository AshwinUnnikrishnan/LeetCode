class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        result = [1] * n
        maxR = 1
        for i in range(n):
            maxL = 0
            for j in range(0, i):
                if nums[j]<nums[i] and maxL<result[j]:
                    maxL = result[j]
            result[i] = maxL + 1
            if maxR < result[i]:
                maxR = result[i]
        return maxR
        
                    