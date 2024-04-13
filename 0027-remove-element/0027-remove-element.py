class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize k to count non-val elements
        for i in range(v:=len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Overwrite nums[k] with non-val element
                k += 1  # Increment k
        return k

                
        
        