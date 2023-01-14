class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        merged = []
        
        for starti, endi in sorted_intervals:
            if starti <= end:
                end = max(end, endi)
            else:
                merged.append([start, end])
                start = starti
                end = endi
        merged.append([start, end])
        return merged
        
