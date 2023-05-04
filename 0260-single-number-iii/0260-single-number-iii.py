class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # XOR all elements to get XOR of two elements that appear only once
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Find a set bit in the XOR result
        set_bit = 0
        while xor_result & (1 << set_bit) == 0:
            set_bit += 1
        
        # Divide elements into two groups based on whether the set bit is set or not
        group1, group2 = 0, 0
        for num in nums:
            if num & (1 << set_bit):
                group1 ^= num
            else:
                group2 ^= num
        
        # Return the two elements that appear only once
        return [group1, group2]
            
        
        
        
        
        
        
        
        # count = Counter(nums)
        # sortd = sorted(count.items(), key=lambda item:item[1])
        # res = sortd[:2]
        # temp = []
        # for item in res:
        #     temp.append(item[0])
        # return temp
        