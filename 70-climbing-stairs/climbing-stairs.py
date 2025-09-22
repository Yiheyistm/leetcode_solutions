class Solution:
    def __init__(self):
        self.memo = [-1] * 46

    def climbStairs(self, n: int) -> int:
        if n == 0:return 1
        elif n <  0: return 0
        if self.memo[n] == -1: self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
