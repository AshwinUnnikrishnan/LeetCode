# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        temp = head
        count = 0
        #len_list = 0
        #while temp:
        #    temp = temp.next
        #    len_list +=1
        
        #temp = head
        
        
        #dictV = [True if v in nums else False for v in range(len_list) ]

        while(temp):
            flag = False
            while temp and temp.val in nums:
                nums.remove(temp.val)
                temp = temp.next
                flag = True
            if temp and temp.val not in nums:
                temp = temp.next
            if flag:
                count += 1
        return count
                
                