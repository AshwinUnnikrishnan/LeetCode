class Solution:
    
    def binarySearch(self, containsList, target):
        #print(containsList)
        low, high = 0, len(containsList)-1
        while low <= high:
            mid = (low+high)//2
            if containsList[mid] == target:
                return True
            elif containsList[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            n = len(matrix[i])
            if matrix[i][0] <= target and matrix[i][n-1]>= target:
                return self.binarySearch(matrix[i], target)
        return False
    
    