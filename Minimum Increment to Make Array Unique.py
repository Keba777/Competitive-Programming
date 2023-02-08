class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        increments = 0
        last_used = -1

        for num in sorted(nums):
            if num <= last_used:
                increments += last_used + 1 - num
                last_used += 1
            else:
                last_used = num
        return increments
