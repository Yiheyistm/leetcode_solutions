class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1] * (n + 1)
        def dfs(i):
            if i == n: return 1
            if s[i] == '0': return 0
            if memo[i] == -1:
                memo[i] = 0
                for j in range(i, min(i+2, n)):
                    if 1 <= int(s[i:j+1]) <= 26:
                        memo[i] += dfs(j + 1)
            return memo[i]
        return dfs(0)

        