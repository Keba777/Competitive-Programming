class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = deque()

        #Count the number of fresh oranges and enqueue the positions of rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        minutes = 0
        while queue and fresh_oranges > 0:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()

                # Check the four adjacent cells individually
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    fresh_oranges -= 1
                    queue.append((x-1, y))
                if x < m-1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    fresh_oranges -= 1
                    queue.append((x+1, y))
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    fresh_oranges -= 1
                    queue.append((x, y-1))
                if y < n-1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    fresh_oranges -= 1
                    queue.append((x, y+1))

            minutes += 1

        return minutes if fresh_oranges == 0 else -1

