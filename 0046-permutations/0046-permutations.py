class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(result, current, remaining):
            
            if len(remaining) == 0:
                result.append(current.copy())
            for i in range(len(remaining)):
                current.append(remaining[i])
                dfs(result, current, remaining[:i] + remaining[i+1:])
                current.pop()
                
        result = []
        dfs(result, [], nums)
        return result