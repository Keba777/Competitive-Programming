class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[0] * n for _ in range(m)]
        
        # Find all the 0s and add them to the queue for BFS
        queue = deque([(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0])
        visited = set(queue)
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    result[nr][nc] = result[r][c] + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return result