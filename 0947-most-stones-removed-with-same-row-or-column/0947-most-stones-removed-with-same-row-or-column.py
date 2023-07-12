class DisjointSet:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        elif self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DisjointSet()
        for x, y in stones:
            dsu.union(x, ~y)

        return len(stones) - len({dsu.find(x) for x, _ in stones})



