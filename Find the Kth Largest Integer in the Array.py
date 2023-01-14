class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = sorted(nums, key=lambda x: (int(x)), reverse=True)
        return arr[k - 1]
