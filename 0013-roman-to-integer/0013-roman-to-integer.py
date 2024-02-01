class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        n = len(s)
        mapV = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        total = 0
        while i<n-1:
            # M CM XCIV      
            if i< n and int(mapV[s[i]]) > int(mapV[s[i+1]]):        # MC
                total += int(mapV[s[i]])
                i += 1
            elif i<n and int(mapV[s[i]]) < int(mapV[s[i+1]]):       # XC
                total += (int(mapV[s[i+1]]) - int(mapV[s[i]]))
                i += 2
            elif i<n and mapV[s[i]] == mapV[s[i+1]]:
                total += mapV[s[i]]
                print(s[i])                                         # CC        
                i += 1
        
        
        if s[n-1] == s[n-2] or int(mapV[s[n-1]]) < int(mapV[s[n-2]]):
            total += mapV[s[n-1]]
        
        
        return(total)
            
            
            