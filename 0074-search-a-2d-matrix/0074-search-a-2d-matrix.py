class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(nums, target):
            left, right = 0, len(nums)-1
            while left<=right:
                
                mid = (left+right)//2

                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False    
        
        
        
        
        left, right = 0, len(matrix)-1

        while left<=right:

            mid = (left+right)//2
            
            if matrix[mid][0] <= target and target<= matrix[mid][len(matrix[mid])-1]:
                return binarySearch(matrix[mid], target)
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False        