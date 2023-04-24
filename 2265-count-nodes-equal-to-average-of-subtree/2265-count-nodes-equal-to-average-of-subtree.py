# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0
            
            left_count, left_sum, left_average = dfs(node.left)
            right_count, right_sum, right_average = dfs(node.right)
            
            curr_count = left_count + right_count + 1
            curr_sum = left_sum + right_sum + node.val
            curr_average = curr_sum // curr_count
            
            return curr_count, curr_sum, left_average + right_average + (node.val == curr_average)
        
        _, _, result = dfs(root)
        return result
