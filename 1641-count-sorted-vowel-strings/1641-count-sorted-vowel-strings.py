class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return ((n+1)*(n+2)*(n+3)*(n+4))//24