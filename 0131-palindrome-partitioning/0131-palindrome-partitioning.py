class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(substring):
            return substring == substring[::-1]

        def dfs(result, current, remaining):
            
            if len(remaining) == 0:
                result.append(current.copy())
                return
            for i in range(1,len(remaining)+1):
                val = remaining[:i]
                if is_palindrome(val):
                    current.append(val)
                    dfs(result, current, remaining[i:])
                    current.pop()
        result = []
        dfs(result, [], s)
        return result
                