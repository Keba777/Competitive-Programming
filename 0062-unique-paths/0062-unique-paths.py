class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D grid to store the number of unique paths
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first row and column with 1, as there is only one way to reach each cell in the first row and column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Calculate the number of unique paths for each cell in the grid
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
       
        return dp[m-1][n-1]