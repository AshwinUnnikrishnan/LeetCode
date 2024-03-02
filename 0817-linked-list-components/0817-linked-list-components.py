class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)  # Convert nums list to a set for faster lookup
        
        count = 0

        temp = head
        while temp:
            if temp.val in nums_set:  # Check if the value is present in nums_set
                count += 1
                while temp and temp.val in nums_set:
                    nums_set.remove(temp.val)
                    temp = temp.next
            else:
                temp = temp.next
        
        return count