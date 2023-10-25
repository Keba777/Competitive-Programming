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
        first_node = None
        second_node = None
        prev_node = TreeNode(float('-inf'))
        stack = []

        # Perform inorder traversal using BFS
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            
            # Check if the current node violates the BST property
            if root.val < prev_node.val:
                if not first_node:
                    first_node = prev_node
                second_node = root
            prev_node = root

            root = root.right

        # Swap the values of the two nodes
        first_node.val, second_node.val = second_node.val, first_node.val

        return root
