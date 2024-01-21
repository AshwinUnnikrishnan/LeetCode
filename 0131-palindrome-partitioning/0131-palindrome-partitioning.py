class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                current_substring = s[start:end]
                if is_palindrome(current_substring):
                    backtrack(end, path + [current_substring])

        result = []
        backtrack(0, [])
        return result