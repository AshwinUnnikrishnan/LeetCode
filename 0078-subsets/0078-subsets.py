class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(result, current, num, val, n):
            
            if val==n:
                result.append(current.copy())
                return
            current.append(num[0])
            dfs(result, current, num[1:],val+1,n)
            current.pop()
            dfs(result, current, num[1:],val+1,n)
        result = []
        dfs(result, [], nums, 0, len(nums))
        return result
        