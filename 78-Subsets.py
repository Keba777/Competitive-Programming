class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        else:
            result = []
            for i in self.subsets(nums[1:]):
                result.append(i)
                result.append([nums[0]] + i)
            return result


