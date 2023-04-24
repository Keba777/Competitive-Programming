from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def backtrack(index, children, max_so_far, min_unfairness):
            if index == len(cookies):
                return max_so_far

            best = min_unfairness
            for i in range(k):
                children[i] += cookies[index]
                new_max_so_far = max(max_so_far, children[i])
                if new_max_so_far < best:
                    best = min(best, backtrack(index + 1, children, new_max_so_far, min_unfairness))
                children[i] -= cookies[index]

            return best

        return backtrack(0, [0] * k, 0, float('inf'))