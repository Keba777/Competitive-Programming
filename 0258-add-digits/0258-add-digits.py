class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        nums = list(str(num))
        total = 0
        for item in nums:
            total = total + int(item)
        return self.addDigits(total)
