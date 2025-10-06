class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @cache
        def dfs(r, c):
            if c < 0 or c > r:
                return 0
            if r == 0 and c == 0:
                return poured
            left = max((dfs(r - 1, c - 1) - 1) / 2, 0)
            right = max((dfs(r - 1, c) - 1) / 2, 0)
            return left + right
        
        return min(1, dfs(query_row, query_glass))
                




            

        