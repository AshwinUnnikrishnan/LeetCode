class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        current_max_reach = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_max_reach:
                jumps += 1
                current_max_reach = farthest
                if current_max_reach >= n - 1:
                    break

        return jumps