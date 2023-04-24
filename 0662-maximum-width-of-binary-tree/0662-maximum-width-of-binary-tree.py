# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = [(root, 1)]
        
        while queue:
            level_length = len(queue)
            level_start = queue[0][1]
            level_end = queue[-1][1]
            max_width = max(max_width, level_end - level_start + 1)
            
            for _ in range(level_length):
                node, position = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2 * position))
                if node.right:
                    queue.append((node.right, 2 * position + 1))
                    
        return max_width
