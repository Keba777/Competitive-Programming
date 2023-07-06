class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(node, quiet, richer_map, res):
            if res[node] == None:
                res[node] = node
                for neighbor in richer_map[node]:
                    cand = dfs(neighbor, quiet, richer_map, res)
                    if quiet[cand] < quiet[res[node]]:
                        res[node] = cand
            return res[node]

        n = len(quiet)
        richer_map = {i: [] for i in range(n)}
        for a, b in richer:
            richer_map[b].append(a)

        res = [None] * n
        for i in range(n):
            if res[i] == None:
                dfs(i, quiet, richer_map, res)

        return res
