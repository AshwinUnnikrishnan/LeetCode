class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n == 0:
            return True
        if m == 0 or n>m:
            return False
        j = 0
        for i in range(m):
            if t[i] == s[j]:
                j += 1
            if j == n:
                break
        if j == n:
            return True
        return False
            
            