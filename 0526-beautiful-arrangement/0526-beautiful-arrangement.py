class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(start, mask):
            if start > n:
                nonlocal count
                count += 1
            for i in range(1, n+1):
                if not (mask & (1 << i)) and (i % start == 0 or start % i == 0):
                    backtrack(start+1, mask | (1 << i))

        count = 0
        backtrack(1, 0)
        return count

