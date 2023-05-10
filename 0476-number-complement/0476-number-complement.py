class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        flipped_bits = ''.join('1' if bit == '0' else '0' for bit in binary)
        return int(flipped_bits, 2)