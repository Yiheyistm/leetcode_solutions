class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        store = [[-1] * n for _ in range(m)]
        def dp(i, j):
            if i == m -1 and j == n -1: return grid[i][j]
            if i >= m or j >= n:
                return float("inf")
            if store[i][j] == -1:
                store[i][j] = min(dp(i + 1, j), dp(i, j + 1)) + grid[i][j]
            return store[i][j]
        return dp(0, 0)
        
        