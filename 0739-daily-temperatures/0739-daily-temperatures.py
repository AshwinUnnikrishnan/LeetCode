class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        i = len(temperatures) - 1
        result = [0] * (i+1)
        
        while i>= 0:
            
            if len(stack) == 0:
                result[i] = 0
                stack.append((temperatures[i], 0))
                i -= 1
                continue
            
            elif stack[-1][0] > temperatures[i]:
                stack.append((temperatures[i], 1))

                result[i] = 1
                i -= 1
                continue
            
            else:
                popCount = 0
                while len(stack) != 0 and stack[-1][0] <= temperatures[i]:
                    v = stack.pop()
                    popCount += v[1]

                if len(stack) != 0:
                    
                    
                    stack.append((temperatures[i], popCount + 1))
                    result[i] = popCount + 1
                    i -= 1

        return result
            
        