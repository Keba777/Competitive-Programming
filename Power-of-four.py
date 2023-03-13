class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True

        return self.isPowerOfFour(n/4)
        # self.n = n
        # if n <= 0:
        #     return False
        # return 4 ** int(math.log(n, 4)) == n
