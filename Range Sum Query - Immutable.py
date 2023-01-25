class NumArray:

    def __init__(self, nums: List[int]):
        self.cumul = [0]
        for num in nums:
            self.cumul.append(self.cumul[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.cumul[right + 1] - self.cumul[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
