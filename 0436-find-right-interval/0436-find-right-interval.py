class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = [intervals[i][0] for i in range(n)]
        starts_idx = sorted(range(n), key=lambda i: starts[i])
        
        def binary_search(target):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if starts[starts_idx[mid]] < target:
                    left = mid + 1
                else:
                    right = mid
            return starts_idx[left] if left < n else -1
        
        return [binary_search(intervals[i][1]) for i in range(n)]