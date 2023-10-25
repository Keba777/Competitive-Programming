class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]

        def is_exit(x, y):
            return (x == 0 or x == m - 1 or y == 0 or y == n - 1) and [x, y] != entrance

        q = deque([(*entrance, 0)]) # (x, y, steps)
        visited[entrance[0]][entrance[1]] = True

        while q:
            x, y, steps = q.popleft()

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == '.':
                    if is_exit(nx, ny):
                        return steps + 1

                    visited[nx][ny] = True
                    q.append((nx, ny, steps + 1))

        return -1
