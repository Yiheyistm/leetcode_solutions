class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        if n == 0 or m == 0:
            return []
        res = []
        l = r = 0
        while l < n and r < m:
            str_f,end_f = firstList[l]
            str_s,end_s = secondList[r]
            mx = max(str_f,str_s)
            mn = min(end_f,end_s)
            if mx <= mn:
                res.append([mx, mn])
            if end_f < end_s:
                l += 1
            else:
                r += 1
        return res





        