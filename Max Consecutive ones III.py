class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        x = 0

        for r,num in enumerate(nums):
            k -= 1-num
            
            if k < 0:
                k += 1-nums[l]
                
                l += 1

            else:
                x = max(x, r-l+1)

        return x

        