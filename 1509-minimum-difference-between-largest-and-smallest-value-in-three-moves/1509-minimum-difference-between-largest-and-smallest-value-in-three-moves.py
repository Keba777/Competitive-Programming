class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        
        min_diff = float('inf')

        # Case 1: Remove the three largest elements
        min_diff = min(min_diff, nums[n-4] - nums[0])

        # Case 2: Remove the two largest elements and the smallest element
        min_diff = min(min_diff, nums[n-3] - nums[1])

        # Case 3: Remove the largest element, the second largest element, and the smallest element
        min_diff = min(min_diff, nums[n-2] - nums[2])

        # Case 4: Remove the largest element, the second smallest element, and the smallest element
        min_diff = min(min_diff, nums[n-1] - nums[3])

        return min_diff