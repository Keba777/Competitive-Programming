class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = row - row % 3, col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True

        def backtrack(row=0, col=0):
            if row == 9:
                return True
            if col == 9:
                return backtrack(row + 1, 0)
            if board[row][col] != ".":
                return backtrack(row, col + 1)
            for num in "123456789":
                if is_valid(row, col, num):
                    board[row][col] = num
                    if backtrack(row, col + 1):
                        return True
                    board[row][col] = "."
            return False

        backtrack()