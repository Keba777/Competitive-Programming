# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getAncestor(root, p, q):
            if root is None:
                return None
            if root == p or root == q:
                return root
                
            left = getAncestor(root.left, p, q)
            right = getAncestor(root.right, p, q)

            if left is not None and right is not None:
                return root
            if left is not None:
                return left
            else:
                return right

        return getAncestor(root, p, q)

        
