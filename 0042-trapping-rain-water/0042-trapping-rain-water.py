class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftMax = height[0]
        rightMax = height[len(height) - 1]
        left = [0]
        right = [0]
        
        
        for i in range(1, len(height)):
            
            left.append(leftMax)
            leftMax = max(leftMax, height[i])
        
            right.insert(0, rightMax)
            rightMax = max(rightMax, height[len(height) - 1 - i])
        
        
        print(left)
        print(right)
        res = 0
        for i in range(len(height)):
            dep = min(left[i], right[i]) 
            if dep > height[i]:
                res += dep - height[i]
                print(res)
        
        return res