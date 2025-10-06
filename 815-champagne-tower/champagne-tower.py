class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = [[-1] * (r +1) for r in range(query_row + 1)]
        def dfs(r, c):
            if c < 0 or c > r:
                return 0
            if r == 0 and c == 0:
                return poured
            if memo[r][c] == -1:
                left = max((dfs(r - 1, c - 1) - 1) / 2, 0)
                right = max((dfs(r - 1, c) - 1) / 2, 0)
                memo[r][c] = left + right
            return memo[r][c]
        return min(1, dfs(query_row, query_glass))
     




            

        