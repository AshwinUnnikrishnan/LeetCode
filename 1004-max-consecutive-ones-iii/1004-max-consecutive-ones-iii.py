class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Maximum length of consecutive 1's
        
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            # If the number of 0's in the window exceeds k, move the left pointer
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
