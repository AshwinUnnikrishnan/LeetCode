class Solution:
    def isValid(self, s: str) -> bool:
        
        stackV = []
        
        i, n = 0, len(s)
        
        while(i<n):
            
            if len(stackV) == 0: 
                if s[i] in [')','}',']']:
                    print("123")
                    return False
                else:
                    stackV.append(s[i])
                    i += 1
            else:   # stack not empty
                if s[i] in [')','}',']']:  # new value is closing
                    if (s[i] == ')' and stackV[-1]!='(') or (s[i] == ']' and stackV[-1]!='[') or (s[i] == '}' and stackV[-1]!='{'):
                        print("ASD")
                        print(i)
                        print(stackV)
                        return False
                    else:
                        stackV.pop()
                        i += 1
                else:
                    stackV.append(s[i])
                    i += 1
        if len(stackV) != 0:
            return False
        return True
            