class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maxTotal = total

        for i in range(len(nums) - k):
            total -= nums[i] 
            total += nums[k + i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k
