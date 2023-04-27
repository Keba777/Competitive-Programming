class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = n < 0
        pos = self.pos_pow(x, abs(n))
        return 1/pos if neg else pos

    def pos_pow(self, x, n):
        if n == 0:
            return 1
        temp = self.pos_pow(x, n//2)
        temp *= temp
        return temp if n % 2 == 0 else temp * x
        
        