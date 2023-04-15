class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        nums.sort()

        result = []
        for i in self.subsetsWithDup(nums[1:]):
            subset = [nums[0]] + i
            if subset not in result:
                result.append(subset)
            if i not in result:
                result.append(i)
        return result
