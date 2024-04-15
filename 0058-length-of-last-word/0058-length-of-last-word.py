class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [val.strip() for val in s.split(" ")]
        
        def filt(word):
            return word if word!='' else None
        words = list(filter(filt, words))
        
        return len((words)[-1])