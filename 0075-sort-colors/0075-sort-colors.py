class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buc = [0] *3
        for i in nums:
            buc[i] += 1
        j = 0
        for i in range(len(nums)):
            while buc[j] == 0:
                j += 1
            nums[i] = j
            buc[j] -= 1
        return nums