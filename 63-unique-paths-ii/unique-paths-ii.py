class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]: return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        store = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == m -1 and j == n - 1:
                return 1
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if store[i][j] == -1:
                store[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return store[i][j]
        return dfs(0, 0)
        