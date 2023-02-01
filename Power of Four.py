class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        self.n = n
        if n <= 0:
            return False
        return 4 ** int(math.log(n, 4)) == n
