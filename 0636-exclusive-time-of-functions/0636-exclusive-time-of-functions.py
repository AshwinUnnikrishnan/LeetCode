class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        def checkStart(val):
            temp = val.split(":")
            if temp[1] == "start":
                return True, int(temp[0]), int(temp[2])
            return False, int(temp[0]), int(temp[2])
            
            
        
        func = [0]*n
        i, n = 0, len(logs)
        stack = []
        
        while i<n:
            start, functionID, timeStamp = checkStart(logs[i])
            
            if len(stack) == 0:
                stack.append([functionID, timeStamp])
            else:
                
                if start:
                    currentStackTopFunctionId = stack[-1][0]
                    func[currentStackTopFunctionId] += timeStamp - stack[-1][1]
                    stack.append([functionID, timeStamp])
                else:
                    currentStackTopFunctionId = stack[-1][0]
                    func[currentStackTopFunctionId] += timeStamp - stack[-1][1] + 1
                    stack.pop()
                    if len(stack)!= 0:
                        stack[-1][1] = timeStamp+1                    
            i += 1
        return func
        
