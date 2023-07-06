class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
        
        def isSafe(row, col):
            # Check if there is no queen in the same column
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False
            
            # Check if there is no queen in the upper left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Check if there is no queen in the upper right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def solveNQueensHelper(row):
            if row == n:
                result.append([''.join(row) for row in chessboard])
                return
            
            for col in range(n):
                if isSafe(row, col):
                    chessboard[row][col] = 'Q'
                    solveNQueensHelper(row + 1)
                    chessboard[row][col] = '.'
        
        solveNQueensHelper(0)
        return result
