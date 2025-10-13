class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapify(intervals)
        ans = []
        while len(intervals) > 1:
            first, second = heappop(intervals),heappop(intervals)
            stF, enF = first
            stS, enS = second
            if enF < stS:
                ans.append(first)
                heappush(intervals, second)
            else:
                heappush(intervals, [stF, max(enS, enF)])

        if intervals:
            p = heappop(intervals)
            ans.append(p)
        return ans


        