class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):
            no_child = 0
            for cd in candies:
                no_child += cd // mid
            return no_child >= k

        l = 0
        h = sum(candies) // k + 1
        while l + 1 < h:
            md = (l + h) // 2
            if check(md):
                l = md
            else: h = md
        return l