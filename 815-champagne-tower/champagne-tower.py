class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0] * 1
        dp[0]= poured
        for r in range(1, query_row + 1):
            dp += [0]
            for c in range(r,-1,-1):
                if c == 0:
                    dp[c] = max((dp[c] - 1) / 2, 0)
                else:
                    dp[c] = max((dp[c] - 1) / 2, 0) + max((dp[c - 1] - 1) / 2, 0)

        return min(1, dp[query_glass])

     




            

        