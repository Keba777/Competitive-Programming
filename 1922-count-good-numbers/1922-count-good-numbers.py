class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 1 if n % 2 == 0 else 5
        x = 20
        i = n // 2
        while i > 0:
            if i % 2 != 0:
                result = (result * x) % MOD
            x = (x ** 2) % MOD
            i //= 2
        return result