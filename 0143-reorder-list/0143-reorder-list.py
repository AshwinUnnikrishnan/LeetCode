# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0
        temp = head
        
        while temp:
            count+= 1
            temp = temp.next
        count = (count-1)//2
        
        i = 0
        temp = head
        while i < count:
            temp = temp.next
            i+=1
        prev = temp
        cur = temp.next
        prev.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        head1 = head
        head2 = prev
        while head2 and head1:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2
        
        return head            
        