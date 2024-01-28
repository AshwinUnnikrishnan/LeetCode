class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left, right = 0,0
        n = len(nums)
        print(nums)
        while right < n:
            
            cur = nums[right]
            i = right + 1
            while i<n and nums[i]==cur:
                i += 1
            num = i - right
            if num>=2:
                num = 2
            
            while right<n and num>0:
                print(right)
                print("Ad")
                nums[left] = nums[right]
                left += 1
                right += 1
                num -= 1
            print(nums)
            right = i
        return left