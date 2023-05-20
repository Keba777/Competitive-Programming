class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city, visited):
            visited.add(city)
            for i, connected in enumerate(isConnected[city]):
                if connected and i not in visited:
                    dfs(i, visited)

        n = len(isConnected)
        visited = set()
        provinces = 0
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city, visited)
        return provinces
