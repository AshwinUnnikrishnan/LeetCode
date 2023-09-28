class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cur_sum = float(sum(nums[:k]))
        n = len(nums) - k
        i = 0
        sum_val = cur_sum
        while n > 0:
            cur_sum = cur_sum - nums[i] + nums[i+k]
            if sum_val < cur_sum:
                sum_val = cur_sum
            n -= 1
            i += 1
        return sum_val/k