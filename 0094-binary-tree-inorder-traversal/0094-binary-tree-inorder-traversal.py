# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node = root
        if node is None:
            return []
        left_node = self.inorderTraversal(node.left)
        right_node = self.inorderTraversal(node.right)
        return left_node + [node.val] + right_node
