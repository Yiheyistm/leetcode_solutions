class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        h = n + 1
        while l + 1 < h:
            m = (l + h) // 2
            if (m * (m + 1)) // 2 <= n:
                l = m
            else: h = m
        return l
        