class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        
        res = []
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
            
        return res