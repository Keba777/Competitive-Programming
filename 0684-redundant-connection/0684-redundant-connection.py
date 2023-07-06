class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        
        for u, v in edges:
            if uf.find(u) == uf.find(v):
                return u, v
            uf.union(u, v)
