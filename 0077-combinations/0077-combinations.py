class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def getCombination(start, k):
            if k == 0:
                return [[]]
            result = []
            for i in range(start, n + 1):
                for comb in getCombination(i + 1, k -1):
                    result.append([i] + comb)
            return result
        return getCombination(1, k)
            