class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        inter = set1 & set2
        
        set1.difference_update(inter)
        set2.difference_update(inter)

        new_num1 = list(set1)
        new_num2 = list(set2)
        return [new_num1, new_num2]
