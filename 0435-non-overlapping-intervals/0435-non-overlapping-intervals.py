class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], x[1]))
        print(intervals)
        a = intervals[0][1]
        result = 0
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            print(f"a {a} , ( {s}, {e}")
            if a > s and a < e or a==e:
                result +=1
            else:
                a=e

        return result
        