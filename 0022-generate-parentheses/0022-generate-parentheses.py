class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def getCombinations(oBCount, cBCount, current, result, n):
            
            if oBCount == n and cBCount == n:
                result.append(current)
            
            if oBCount < n:
                getCombinations(oBCount+1, cBCount, current+"(", result, n)
            
            if cBCount < oBCount and cBCount < n:
                getCombinations(oBCount, cBCount+1, current+")", result, n)
            
        result = []
        getCombinations(0,0,"", result,n)
        return result

        