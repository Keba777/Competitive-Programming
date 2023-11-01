class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        result = [1] * n

        for i in range(1, n):
            prefix *= nums[i - 1]
            result[i] *= prefix

            suffix_i = n - i - 1
            suffix *= nums[suffix_i + 1]
            result[suffix_i] *= suffix

        return result
        