class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            result |= (count % 3) << i
        return result if result < 2**31 else result - 2**32
            
        
        
        
        
        
        
        # count = Counter(nums)
        # sortd = [sorted(count.items(), key=lambda item:item[1])]
        # res = sortd[0][0]
        # return res[0]