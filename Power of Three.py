class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        self.n = n
        if n <= 0:
            return False

        max_int = 2 ** 31 - 1
        max_pow = int(math.log(max_int, 3))
        return 3 ** max_pow % n == 0
