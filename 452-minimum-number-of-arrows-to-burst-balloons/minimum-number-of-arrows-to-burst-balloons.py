class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x [1])
        noArr = 0
        ovrp = points[0][1]
        for i in range(1, len(points)):
            s, e = points[i]
            if s <= ovrp <= e: continue
            else:
                noArr += 1
                ovrp = e
        noArr += 1
        return noArr

        