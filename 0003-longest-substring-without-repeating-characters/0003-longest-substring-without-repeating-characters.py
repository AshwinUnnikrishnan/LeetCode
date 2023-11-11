class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        curMax = 0  # Initialize the maximum length to 0
        curV = set()  # Use a set to keep track of unique characters
        l, r = 0, 0

        while r < n:
            if s[r] not in curV:
                curV.add(s[r])
                curMax = max(curMax, r - l + 1)
                r += 1
            else:
                curV.remove(s[l])
                l += 1

        return curMax
            