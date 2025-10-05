class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        # dp = [0] * (N + 2)
        # for i in range(N-1, -1, -1):
        #         dp[i] = dp[i + 1] # skip
        #         for j in range(i+1, N):
        #             if prices[j] >= prices[i]:
        #                 dp[i] = max(dp[i], prices[j] - prices[i] + dp[j + 2]) # sell at j that are buy at i
        # return dp[0]
        dp = {}
        def dfs(i, buying):
            if i >= N: return 0

            if (i, buying) not in dp:
                cooldown = dfs(i+1, buying)
                if buying:
                    buy = dfs(i+1, not buying) - prices[i]
                    dp[(i, buying)] = max(cooldown, buy)
        
                else:
                    sell = dfs(i+2, not buying) + prices[i]
                    dp[(i, buying)] = max(cooldown, sell)
            return dp[(i, buying)]
        return dfs(0, True)
        