class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
    
        # Precompute onesRow and onesCol
        onesRow = [sum(row) for row in grid]  # Count of 1s in each row
        onesCol = [sum(grid[i][j] for i in range(m)) for j in range(n)]  # Count of 1s in each column
        
        # Create the diff matrix
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * onesRow[i] + 2 * onesCol[j] - m - n
        
        return diff