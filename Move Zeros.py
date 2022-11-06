class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)

        nex = 0

        for n in nums:
            if n != 0:
                nums[nex] = n 
                nex += 1

        for zero in range(1, zero_count + 1):
            nums[-zero] = 0