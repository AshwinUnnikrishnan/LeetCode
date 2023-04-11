# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0, None)
        resultP = result
        prevRes = None
        while l1 != None and l2!= None:
            
            curSum = l1.val + l2.val + carry
            result.val = curSum % 10
            result.next = ListNode(0, None)
            prevRes = result
            result = result.next
            carry = curSum//10

            l1 = l1.next
            l2 = l2.next
        
        if l1 == None:
            l1 = l2
        
        while l1 != None:
            curSum = l1.val + carry
            result.val = curSum % 10
            result.next = ListNode(0, None)
            prevRes = result
            result = result.next
            carry = curSum//10
            l1 = l1.next
        if carry == 1:
            result.val = 1
        else:
            prevRes.next = None
        return resultP