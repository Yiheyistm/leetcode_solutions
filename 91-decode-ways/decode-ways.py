class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] * (n + 1)
        dp[-2] = 1 if s[-1] != '0' else 0
        for i in range(n - 2, -1, -1):
            if s[i] == '0': dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                dp[i] += dp[i + 2] if 1 <= int(s[i:i+2]) <= 26 else 0
        return dp[0]




        