class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_sizes = {}  # Mapping of island_id to its size
        island_id = 2  # Start from 2 to distinguish from 1 in grid

        def dfs(i, j, island_id):
            """Performs DFS to find island size and mark it with an island_id."""
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = island_id
            size = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                size += dfs(i + di, j + dj, island_id)
            return size

        # Step 1: Find all islands and assign unique IDs
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1

        # Step 2: Find the largest possible island by converting a 0 to 1
        max_island = max(island_sizes.values(), default=0)  # Maximum existing island size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # Check all unique neighboring islands
                    seen = set()
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])  # Collect unique island IDs

                    # Compute potential new island size
                    new_size = 1 + sum(island_sizes[iid] for iid in seen)
                    max_island = max(max_island, new_size)

        return max_island