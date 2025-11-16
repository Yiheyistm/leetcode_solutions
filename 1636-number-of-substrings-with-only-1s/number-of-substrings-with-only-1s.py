class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] == '0':
                l = r + 1
            res += r - l + 1
        return res % MOD