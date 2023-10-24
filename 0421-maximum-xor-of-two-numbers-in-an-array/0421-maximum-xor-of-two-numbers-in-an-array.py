class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        for i in range(30, -1, -1):
            mask |= (1 << i)
            prefix = set()
            for num in nums:
                prefix.add(num & mask)
            
            found = False
            new_xor = max_xor | (1 << i)
            for pref in prefix:
                if new_xor ^ pref in prefix:
                    found = True
                    break
            
            if found:
                max_xor = new_xor
        
        return max_xor