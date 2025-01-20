class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # Map each number to its (row, col) position
        num_to_pos = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}
        
        # Arrays to count painted cells in rows and columns
        rowCount = [0] * m
        colCount = [0] * n
        
        # Process each number in arr
        for i, num in enumerate(arr):
            row, col = num_to_pos[num]
            rowCount[row] += 1
            colCount[col] += 1
            
            # Check if a row or column is fully painted
            if rowCount[row] == n or colCount[col] == m:
                return i
        
        # This should not be reached if the inputs are valid
        return -1