class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = 0
        def isEven(num):
            num = str(num)
            count = len(num)
            return count % 2 == 0
        for num in nums:
            n +=  isEven(num)

        return n
