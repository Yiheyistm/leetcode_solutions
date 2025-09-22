class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def dp(n):
            if n == 1 or n == 0: return n
            if memo[n] == -1:
                memo[n] = self.fib(n -1) + self.fib(n - 2)
            return memo[n]
        return dp(n)
        