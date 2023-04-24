# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def findSum(root, currentSum):
            if not root:
                return 0
            currentSum += root.val
            count = 1 if currentSum == targetSum else 0
            count += findSum(root.left, currentSum) + findSum(root.right, currentSum)
            return count
        
        count = findSum(root, 0)
        count += self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        
        return count


        