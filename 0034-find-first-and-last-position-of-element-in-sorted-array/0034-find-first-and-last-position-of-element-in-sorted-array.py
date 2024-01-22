class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if left < len(nums) and nums[left] == target else -1

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2 + 1  # Make mid biased to the right
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return left if nums[left] == target else -1

        first, last = findFirst(nums, target), findLast(nums, target)
        return [first, last]