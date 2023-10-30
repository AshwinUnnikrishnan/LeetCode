from collections import Counter

class Solution:
    def findOriginalArray(self, changed):
        n = len(changed)
        
        if n % 2 == 1:
            return []
        
        # Count the occurrences of each element in the changed array
        count = Counter(changed)
        
        original = []
        
        for num in sorted(changed):
            if count[num] == 0:  # This element has already been paired
                continue
            
            if num == 0:
                if count[num] % 2 != 0:  # Zero cannot be doubled
                    return []
                original += [0] * (count[num] // 2)
                count[num] = 0
            elif num * 2 in count and count[num * 2] > 0:
                original.append(num)
                count[num] -= 1
                count[num * 2] -= 1
            else:
                return []  # No valid pair found
            
        return original
