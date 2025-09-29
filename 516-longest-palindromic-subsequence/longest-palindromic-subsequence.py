class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+1) for _ in range(n +1)]
        for i in range(n):
            dp[i][i] = 1

        for l in range(1, n):
            for r in range(l-1, -1, -1):
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l -1][r +1]
                else:
                    dp[l][r] = max(dp[l - 1][r], dp[l][r + 1])
            
        return dp[len(s) - 1][0]

            
        