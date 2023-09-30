class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer of the sliding window
        zero_count = 0  # Count of 0's in the current window
        max_length = 0  # Maximum length of consecutive 1's
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If the number of 0's in the window exceeds k, move the left pointer
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
