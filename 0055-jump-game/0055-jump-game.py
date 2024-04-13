class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        l = len(nums)
        
        reach = [False] * l
        reach[l-1] = True
        i = l-2
        while i>= 0:
            
            if nums[i] == 0:
                i -= 1
                continue
            jumps = range(1, min(l - 1 - i, nums[i]) + 1)  # Adjusted range
            
            for val in jumps:
                if reach[i+val] == True:
                    reach[i] = True
                    break
            
            i -= 1
        return reach[0]
                