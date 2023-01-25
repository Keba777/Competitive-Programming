class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumdict = {0:1}
        n = len(nums)
        count = 0 
        curSum = 0 

        for num in nums:
           curSum += num 
           diff = curSum - k
           count += sumdict.get(diff, 0)
           sumdict[curSum] = 1 + sumdict.get(curSum, 0)


        return count
