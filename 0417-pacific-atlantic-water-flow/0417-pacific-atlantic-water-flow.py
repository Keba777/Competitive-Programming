class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, ocean, visited):
            visited[r][c] = True
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean, visited)

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            dfs(i, 0, pacific, pacific)
            dfs(i, cols - 1, atlantic, atlantic)

        for j in range(cols):
            dfs(0, j, pacific, pacific)
            dfs(rows - 1, j, atlantic, atlantic)

        result = [[i, j] for i in range(rows) for j in range(cols) if pacific[i][j] and atlantic[i][j]]
        return result
