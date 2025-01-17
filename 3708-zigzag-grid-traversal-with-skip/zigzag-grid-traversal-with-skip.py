class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = []
        skip = False  # Variable to track whether to skip a cell

        for i in range(m):
            # Traverse right for even rows, left for odd rows
            if i % 2 == 0:
                for j in range(n):
                    if not skip:
                        result.append(grid[i][j])
                    skip = not skip  # Toggle skip after every cell
            else:
                for j in range(n - 1, -1, -1):
                    if not skip:
                        result.append(grid[i][j])
                    skip = not skip  # Toggle skip after every cell

        return result