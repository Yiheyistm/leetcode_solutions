class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def dp(st):
            if st == n:
                return 1
            elif st > n: return 0

            if memo[st] == -1:
                memo[st] = dp(st + 1) + dp(st + 2)
            return memo[st]
        return dp(0)