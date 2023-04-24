# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted is found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.val = self.minValueNode(root.right).val
                root.right = self.deleteNode(root.right, root.val)
        
        return root

    def minValueNode(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left is not None:
            current = current.left
        return current


