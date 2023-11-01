class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, num in enumerate(nums):
            if target - num in dictionary:
                return [dictionary[target - num], index]
            dictionary[num] = index
        return []

                               