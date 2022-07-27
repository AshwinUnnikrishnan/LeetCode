class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if target < nums[0] or target > nums[len(nums) - 1]:
            return [-1,-1]
        l, h = 0, len(nums) - 1
        res = [-1,-1]
        while l <= h:
            mid = (l+h)//2
            if target == nums[mid]:
                res[1] = mid
                l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l+h)//2
            if target == nums[mid]:
                res[0] = mid
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                h = mid - 1
        return res