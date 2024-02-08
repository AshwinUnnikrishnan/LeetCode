class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mainDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        
        def dfs(result, curr, digit, i, n):
            if i == n:
                result.append(curr)
                return
            strV = mainDict[digit[0]]
            for k in range(len(strV)):
                dfs(result, curr+strV[k], digit[1:],i+1, n)
        result = []
        dfs(result, "", digits, 0, len(digits))
        return result