# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        values = []
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                values.append(node.val)
                inorder(node.right)
                
        inorder(root)
        
        values.sort()
        swap1, swap2 = None, None
        for i in range(len(nodes)):
            if nodes[i].val != values[i]:
                if swap1 is None:
                    swap1 = nodes[i]
                else:
                    swap2 = nodes[i]
                    break
                    
        swap1.val, swap2.val = swap2.val, swap1.val

        