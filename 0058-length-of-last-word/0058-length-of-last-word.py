class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [val.strip() for val in s.split(" ")]
        
        def filt(word):
            return word if word!='' else None
        words = filter(filt, words)
        words = list(words)
        print(words)
        print(len(words))

        print(type(words))
        print(words[-1])
        return len((words)[-1])