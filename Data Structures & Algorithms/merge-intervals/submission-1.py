class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        start, end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            x, y = intervals[i][0], intervals[i][1]
            if x <= end:
                end = max(end, y)
            else:
                res.append([start, end])
                start = x
                end = y

        res.append([start, end])
        return res