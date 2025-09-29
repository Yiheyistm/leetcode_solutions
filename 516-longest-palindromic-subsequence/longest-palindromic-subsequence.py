class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        def dp(l, r):
            if l == r:
                return 1
            if l > r:
                return 0
            if memo[l][r] == -1:
                if s[l] == s[r]:
                    memo[l][r] = 2 + dp(l +1, r -1)
                else:
                    memo[l][r] = max(dp(l + 1, r), dp(l, r - 1))
            return memo[l][r]
        return dp(0, len(s) - 1)
            
        