class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 2 ** 32 - 1
        max_int = 2 ** 31 - 1

        while b != 0:
            total = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = total, carry
        return a if a < max_int else ~(a ^ mask)


