class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        min_value = min(nums)
        max_value = max(nums)
        
        integer_map = {key: 0 for key in range(min_value, max_value+1)}
        
        n = len(nums)
        result = [0] * n
        
        for val in nums:
            integer_map[val] += 1
        
        same_value_flag = False
        
        for i in range(n):
            
            value = 1
            
            for j in range(min_value, max_value+1):
                
                if j == nums[i]:
                    same_value_flag = True
                    integer_map[j] -= 1
                
                if integer_map[j] != 0:
                    value = value * pow(j, integer_map[j])
                
                if same_value_flag:
                    same_value_flag = False
                    integer_map[j] += 1

            result[i] = value
        
        return result