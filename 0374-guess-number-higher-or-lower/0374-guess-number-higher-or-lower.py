# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n+1
        i = (low+high)//2
        
        while i>=low and i<=high:
            flag = guess(i)
            
            if flag == 0:
                return i
            elif flag == 1:
                low = i+1
            else:
                high = i-1
            i = (low+high)//2
 
            