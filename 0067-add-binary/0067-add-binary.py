class Solution:
    def addBinary(self, a: str, b: str) -> str:
        integer = int(a, 2) + int(b, 2)
        return bin(integer)[2:]