# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        positions = defaultdict(list) 
        def dfs(node, row, col):
            if not node:
                return
            positions[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0) 

        result = []
        for col in sorted(positions.keys()):
            result.append([val for row, val in sorted(positions[col])])
        return result