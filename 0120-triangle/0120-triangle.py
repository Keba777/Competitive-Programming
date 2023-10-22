class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        if n == 0:
            return 0
        dp = triangle[-1][:]

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(triangle[i][j] + dp[j], triangle[i][j] + dp[j + 1])

        return dp[0]