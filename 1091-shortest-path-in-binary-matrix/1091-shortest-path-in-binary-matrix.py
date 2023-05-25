class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        n = len(grid)
        dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        visited = set([(0, 0)])
        queue = deque([((0, 0), 1)])  # ((x, y), steps)

        while queue:
            (x, y), steps = queue.popleft()
            if (x, y) == (n - 1, n - 1):
                return steps
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny] and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))
        
        return -1

            