class Solution:
    def canCross(self, stones: List[int]) -> bool:
        pos = {num:i for i, num in enumerate(stones)}

        n = len(stones)
        @cache
        def dp(i, k):
            if i == n -1:
                return True
            if i >= n: return False
            valid = False
            for jump in range(k-1, k+2):
                if jump < 1:continue
                if stones[i] + jump in pos:
                    valid |= dp(pos[stones[i]+jump], jump)
            return valid
        return dp(0, 0)

        