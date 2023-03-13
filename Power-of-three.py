class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True

        return self.isPowerOfThree(n/3)
        # self.n = n
        # if n <= 0:
        #     return False

        # max_int = 2 ** 31 - 1
        # max_pow = int(math.log(max_int, 3))
        # return 3 ** max_pow % n == 0
