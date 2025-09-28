class Solution:
    def canCross(self, stones: List[int]) -> bool:
        pos = {num:i for i, num in enumerate(stones)}
        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            for k in dp[i]:
                for jump in [k-1, k, k+1]:
                    if jump <= 0: continue
                    nxt_jump = stones[i] + jump
                    if nxt_jump in pos:
                        dp[pos[nxt_jump]].add(jump)
        return len(dp[-1]) > 0
       





        