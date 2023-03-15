class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            if k == 1:
                return "0"
            return None

            
        mid = 2**(n-1)
        if k == mid:
            return "1"

        if k < mid:
            return self.findKthBit(n-1, k)
            
            
        else:
            bit = self.findKthBit(n-1, 2**n - k)
           
            if bit is None: 
                return None
            else:
                if bit == "0":
                    return "1"
                return "0"

       
