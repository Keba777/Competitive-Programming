class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        final = []
        for i in range(len(r)):
            temp = sorted(nums[l[i]: r[i] + 1])
            is_arithmetic = True
            for k in range(1, len(temp)):
                if temp[k] - temp[k - 1] != temp[1] - temp[0]:
                    is_arithmetic = False
            final.append(is_arithmetic)
        return final
