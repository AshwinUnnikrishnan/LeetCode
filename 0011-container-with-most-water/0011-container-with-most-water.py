class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxv = -1
        left = 0
        right = len(height) - 1
        
        while left<right:
            
            val = min(height[left], height[right]) * (right-left)
            maxv = max(val, maxv)
            if height[left]<height[right]:
                
                left += 1
            else:
                right -= 1
            
        return maxv