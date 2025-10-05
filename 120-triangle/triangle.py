class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = triangle[:]
        for i in range(N-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j + 1])
        return dp[0][0]
        