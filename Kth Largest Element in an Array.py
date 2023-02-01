class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort_arr = sorted(nums, reverse=True)

        for index, item in enumerate(sort_arr):
            if k == index + 1:
                return item
