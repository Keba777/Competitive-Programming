class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        temp = []
        for i in range(len(nums)):
            if nums[i] == target: 
                temp.append(i)
        return temp
