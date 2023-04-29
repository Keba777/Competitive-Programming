class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(nums, mid):
            left_sum = float('-inf')
            right_sum = float('-inf')
            curr_sum = 0
            
            for i in range(mid-1, -1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)
            
            curr_sum = 0
            for i in range(mid, len(nums)):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            return left_sum + right_sum

        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        
        left_max = self.maxSubArray(nums[:mid])
        right_max = self.maxSubArray(nums[mid:])
        
        cross_max = helper(nums, mid)
        return max(left_max, right_max, cross_max)
        
    



        # overall_max = float('-inf')
        # max_end = 0
        # for num in nums:
        #     if max_end > 0:
        #         max_end += num
        #     else:
        #         max_end = num
        #     overall_max = max(overall_max, max_end)
        # return overall_max
