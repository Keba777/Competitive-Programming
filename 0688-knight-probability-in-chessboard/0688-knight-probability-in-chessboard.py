class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
         # Possible moves for a knight
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        r = row
        c = column
        K = k
        # Initialize the probability grid
        dp = [[0] * n for _ in range(n)]
        dp[r][c] = 1

        # Perform K moves
        for _ in range(K):
            new_dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for move in moves:
                        new_i = i + move[0]
                        new_j = j + move[1]
                        if 0 <= new_i < n and 0 <= new_j < n:
                            new_dp[new_i][new_j] += dp[i][j] / 8
            dp = new_dp

        # Calculate the probability of staying on the board
        probability = 0
        for row in dp:
            probability += sum(row)

        return probability