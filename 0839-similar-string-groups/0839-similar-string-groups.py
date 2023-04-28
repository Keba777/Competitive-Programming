class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                if diff > 2:
                    return False
            return True

        n = len(strs)
        parent = list(range(n))

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(i+1, n):
                if isSimilar(strs[i], strs[j]):
                    union(i, j)

        return sum(i == find(i) for i in range(n))
