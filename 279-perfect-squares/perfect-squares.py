class Solution:
    def numSquares(self, n: int) -> int:
        N = int(sqrt(n)) + 1
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, N):
            for rem in range(i**2, n +1):
                dp[rem] = min(dp[rem], dp[rem - i**2] + 1)

        return dp[n]
        # cause MLE
        # @cache
        # def dfs(i, rem):
        #     if rem == 0:
        #         return 0
        #     if rem < 0 or i >= N:
        #         return inf
        #     leave = dfs(i+1, rem)
        #     take_and_stay = inf
        #     if rem - (i**2) >= 0:
        #         take_and_stay = dfs(i, rem - (i**2))
        #         if take_and_stay != inf:
        #             take_and_stay += 1
        #     return min(leave, take_and_stay)
        # return dfs(1, n)


        
        