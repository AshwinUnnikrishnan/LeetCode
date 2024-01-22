class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        j = 0
        def swap(i,j):
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
    
        while i<n:
            
            if nums[i] != 0:
                swap(i,j)
                j += 1
            i += 1
