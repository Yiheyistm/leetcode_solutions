class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: (item[1], -item[0]))
        p1, p2 = intervals[0][1]-1, intervals[0][1]
        count = 2
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            inside = (p1 >= s) + (p2 >= s)
            if inside == 2: continue
            elif inside == 1:
                count += 1
                p2, p1 = e, p2
            elif s > p2:
                count += 2
                p1 = e-1
                p2 = e
        return count
        