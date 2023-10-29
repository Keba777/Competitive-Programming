class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
    
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        counts = [0] * n
        
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    counts[i] += 1
        
        min_count = float('inf')
        city = -1
        for i in range(n):
            if counts[i] <= min_count:
                min_count = counts[i]
                city = i
        
        return city