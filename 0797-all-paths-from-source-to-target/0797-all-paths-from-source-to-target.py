class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        target = n - 1
        paths = []
        
        queue = deque([(0, [0])])
        
        while queue:
            node, path = queue.popleft()
            
            if node == target:
                paths.append(path)
            
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
        
        return paths
