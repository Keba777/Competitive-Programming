class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_x_y = x ^ y
        count = bin(xor_x_y).count('1')
        return count