# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Build a graph using a dictionary
        graph = {}
        self.buildGraph(root, None, graph)
        
        # Step 2: Perform a breadth-first search starting from the target node
        queue = [(target, 0)]
        visited = set([target])
        result = []
        
        while queue:
            node, distance = queue.pop(0)
            
            if distance == k:
                result.append(node.val)
            
            if distance > k:
                break
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        
        return result
    
    def buildGraph(self, node, parent, graph):
        if not node:
            return
        
        if node not in graph:
            graph[node] = []
        
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        
        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)
