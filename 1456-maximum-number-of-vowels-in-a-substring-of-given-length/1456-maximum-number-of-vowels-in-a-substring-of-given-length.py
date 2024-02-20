class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        def checkVowel(c):
            if c in ['a','e','i','o','u']:
                return True
            return False
        
        lis = []
        
        for i in range(len(s)):
            if checkVowel(s[i]):
                lis.append(True)
            else:
                lis.append(False)
        print(lis)
        l = min(len(s), k)
        count = 0
        for i in range(l):
            if lis[i]:
                count += 1
        if l == len(s):    
            return count
        
        print(count)
        res = count
        for i in range(k, len(s)):
            #if (lis[i-k] and lis[k]) :
            #    continue
            if lis[i]:
                count += 1
            if lis[i-k]:
                count -= 1
            if count > res:
                res = count
            print(res)
        
        
                
                
        
        return res
        