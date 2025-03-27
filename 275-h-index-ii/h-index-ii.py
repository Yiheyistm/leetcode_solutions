class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def checker(mid):
            idx = bisect_left(citations, mid)
            return idx < n and n - idx >= mid

        n = len(citations)
        l = 0
        h = 10 ** 5
        while l + 1 < h:
            mid = (l + h) // 2
            if checker(mid):
                l = mid
            else:
                h = mid
        return l

