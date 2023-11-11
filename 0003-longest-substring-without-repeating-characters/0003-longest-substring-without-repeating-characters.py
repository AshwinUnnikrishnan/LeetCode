class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n == 0:
            return 0
        l,r = 0, 1
        curMax = 1
        curV = set()
        curV.add(s[0])
        
        while r < n:
            print(r)
            if s[r] not in curV:
                curV.add(s[r])
                #print(f"{r} - {l}")
                curMax = max(curMax, r - l + 1)
            else:
                while l< n and s[l] != s[r]:
                    curV.remove(s[l])
                    l += 1
                #curV.remove(s[l])
                l += 1
            r += 1

            print(curV)
            print(s[l:r])
        return curMax
            