class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = len(s)
        if temp == 1 or temp == 0:
            return temp
        start = maxlen = 0
        temp = {}
        for i in range(len(s)):
            if s[i] in temp and start <= temp[s[i]]:
                start = temp[s[i]] + 1
            else:
                maxlen = max(maxlen, i - start + 1)
            temp[s[i]] = i
        return maxlen
    
        