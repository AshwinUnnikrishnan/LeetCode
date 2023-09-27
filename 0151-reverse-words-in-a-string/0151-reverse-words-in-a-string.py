class Solution:
    def reverseWords(self, s: str) -> str:
        
        reverse_s = s[::-1]
        
        
        i = 0
        while(reverse_s[i] == ' '):
            i += 1
        
        j = len(reverse_s) - 1
        while(reverse_s[j] == ' '):
            j -= 1
        
        curr_insert_pos = 0
        result = []
        
        k = i
        print(reverse_s)
        while k<=j:
            while (k<=j and reverse_s[k] != ' '):
                result.insert(curr_insert_pos, reverse_s[k])
                k += 1
            if k<=j and reverse_s[k] == ' ':
                curr_insert_pos = len(result)
                result.insert(curr_insert_pos, reverse_s[k])
                curr_insert_pos = len(result)

            while k<=j and reverse_s[k] == ' ':
                k += 1

       
        return ''.join(result)