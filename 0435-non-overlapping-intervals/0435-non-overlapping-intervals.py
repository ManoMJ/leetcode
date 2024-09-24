class Solution:
    def eraseOverlapIntervals(self,intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        answer = 0
        last_end_time = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end_time:
                answer += 1
            else:
                last_end_time = intervals[i][1]

        return answer