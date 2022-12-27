class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for item in nums:
            if item in temp:
                temp[item] += 1
            else:
                temp[item] = 1

        num_sorted = sorted(temp.items(), key=lambda item:item[1], reverse=True)
        max_item = [*num_sorted[0]]
        if max_item[1] > 1:
            return True
        return False
