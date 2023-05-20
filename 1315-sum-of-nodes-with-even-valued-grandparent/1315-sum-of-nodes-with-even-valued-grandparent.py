# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = []
        def dfs(root):
            if not root:
                return
            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        result.append(root.left.left.val)
                    if root.left.right:
                        result.append(root.left.right.val)
                if root.right:
                    if root.right.left:
                        result.append(root.right.left.val)
                    if root.right.right:
                        result.append(root.right.right.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return sum(result)
