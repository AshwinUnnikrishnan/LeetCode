# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root
        
        if p.val > q.val:
            p,q = q,p
        
        while temp:
            if p.val<= temp.val and q.val>= temp.val:
                return temp
            if p.val<temp.val and q.val<temp.val:
                temp = temp.left
            else:
                temp = temp.right
        