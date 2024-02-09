class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(result, current, remaining):
            nums.sort()
            if len(remaining) == 0:
                result.append(current.copy())
            
            i = 0
            n = len(remaining)
            while i< n:
                current.append(remaining[i])
                dfs(result, current, remaining[:i] + remaining[i+1:])
                current.pop()
                i += 1
                while i<n and (remaining[i-1] == remaining[i]):
                    i+=1
                
        result = []
        dfs(result, [], nums)
        return result