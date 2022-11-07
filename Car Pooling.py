class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        passChange = [0] * 1001

        for t in trips:
            numPass, start, end = t
            passChange[start] += numPass
            passChange[end] -= numPass

        curPass = 0
        for i in range(1001):
            curPass += passChange[i]
            if curPass > capacity:
                return False
        return True
