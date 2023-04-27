
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def division_sum(divisor):
            return sum(math.ceil(num / divisor) for num in nums)

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2
            if division_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid

        return left

