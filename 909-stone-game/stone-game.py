class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * (n) for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        for d in range(1, n):
            for l in range(n - d):
                r = l + d
                dp[l][r] = max(piles[l] - dp[l + 1][r], piles[r] - dp[l][r - 1])
            
        return dp[0][n-1] > 0


        # Top-Down Dp
        # def dfs(i,j):
        #     if i == j:
        #         return piles[i]
        #     left = piles[i] - dfs(i+1, j)
        #     right = piles[j] - dfs(i, j-1)
        #     return max(left, right)
        # return dfs(0, N-1) > 0

        