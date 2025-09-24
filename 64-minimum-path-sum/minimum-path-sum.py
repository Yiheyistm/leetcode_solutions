class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        def topInbound(i,j):
            return dp[i][j] if i >= 0 else float("inf")
        def leftInbound(i, j):
            return dp[i][j] if j >= 0 else float("inf")

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                top = topInbound(i-1, j)
                left = leftInbound(i, j -1)
                dp[i][j] = min(left, top) + grid[i][j]
        return dp[-1][-1]
        