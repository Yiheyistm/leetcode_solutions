class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')] * n 
        dp[0]=grid[0][0]
        for i in range(m):
            for j in range(n):
                if j == 0 and i > 0:
                    dp[0] += grid[i][0]
                elif j > 0: 
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]
        