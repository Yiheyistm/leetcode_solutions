class Solution:
    def canCross(self, stones: List[int]) -> bool:
        pos = {num:i for i, num in enumerate(stones)}

        n = len(stones)
        memo =[[-1]* (n) for _ in range(n)]
        def dp(i, k):
            if i == n -1:
                return True
            if i >= n: return False
            if memo[i][k] == -1:
                valid = False
                for jump in range(k-1, k+2):
                    if jump < 1:continue
                    if stones[i] + jump in pos:
                        valid |= dp(pos[stones[i]+jump], jump)
                memo[i][k] = valid
            return memo[i][k]
        return dp(0, 0)

        