class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index,item in enumerate(nums):
            res = target - item
            if res in dic:
                return [dic[res], index]
            dic[item] = index