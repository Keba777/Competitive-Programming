class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for item in nums:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1

        for key, value in dic.items():
            if value > (len(nums) / 2):
                return key
