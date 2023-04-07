# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def helperDFS(node, cur_path, paths):
            if node.left == None and node.right == None:
                paths.append(cur_path + str(node.val))
                return

            if node.left:
                helperDFS(node.left, cur_path + str(node.val) + "->", paths)
            
            if node.right:
                helperDFS(node.right, cur_path + str(node.val) + "->", paths)

        if root == None:
            return []
        else:
            paths = []
            helperDFS(root, "", paths)
            return paths
