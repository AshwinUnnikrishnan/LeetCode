class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # If array is empty, there are no unique elements

        k = 1  # Initialize k to count unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Overwrite nums[k] with unique element
                k += 1  # Increment k
        return k