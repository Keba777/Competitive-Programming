class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(n, n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return steps
        
        current = 1
        k -= 1
        
        while k > 0:
            steps = count_steps(n, current, current + 1)
            
            if k >= steps:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        
        return current
