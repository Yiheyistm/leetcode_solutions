class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]: return 0
        # TOP-Down dp
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # store = [[-1] * n for _ in range(m)]
        # def dfs(i, j):
        #     if i == m -1 and j == n - 1:
        #         return 1
        #     if i >= m or j >= n or obstacleGrid[i][j] == 1:
        #         return 0
        #     if store[i][j] == -1:
        #         store[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
        #     return store[i][j]
        # return dfs(0, 0)

        # Bottom Up DP
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for j in range(n): # set the first row to one if the dont have obstacle
            if obstacleGrid[0][j]: break
            dp[0][j] = 1 
        for j in range(1, m): # set the first column to one if the dont have obstacle
            if obstacleGrid[j][0]: break
            dp[j][0] = 1


        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j -1]
        return dp[-1][-1]
                
        