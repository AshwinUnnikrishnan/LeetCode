class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            
            mid = (left+right)//2
            
            if nums[left]<=nums[mid] and nums[mid]<= nums[right]:
                print("ASD")
                return nums[left]
            
            elif nums[mid] > nums[mid+1]:
                print("QWE")
                return nums[mid+1]
            
            elif nums[mid] < nums[mid-1]:
                print("!@#!@#!")
                return nums[mid]
            
            elif nums[mid] > nums[left]:
                left = mid+1
            else:
                right = mid - 1
        
            