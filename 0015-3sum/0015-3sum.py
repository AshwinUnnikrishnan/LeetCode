class Solution:

            
            
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            
        def twoSum(nums, target):
            left, right = 0, len(nums) - 1
            result = []
            while left < right:

                tot = nums[left] + nums[right]

                if tot == target:
                    result.append([0-target, nums[left], nums[right]])
                    left += 1
                    while left<right and nums[left-1] == nums[left]:
                        left += 1
                elif tot < target:
                    left += 1
                else:
                    right -= 1
            return result
                
        temp = nums.sort()
        result = []
        i = 0
        while i < len(nums):
            res = twoSum( nums[i+1:] ,0 - nums[i])
            if res:
                result += res
            i += 1
            while i< len(nums) and nums[i-1] == nums[i]:
                i += 1

        
        return result