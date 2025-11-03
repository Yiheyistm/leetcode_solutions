class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = [None, inf]
        res = 0
        for c, t in zip(colors, neededTime):
            if prev[0] == c:
                res += min(prev[1], t)
                prev[1] = max(prev[1], t)
            else:
                prev = [c, t]
        return res
        