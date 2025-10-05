class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        memo = [-1] * N
        def dfs(i):
            if i >= N:
                return 0
            if memo[i] == -1:
                memo[i] = dfs(i + 1) # skip
                for j in range(i+1, N):
                    if prices[j] >= prices[i]:
                        memo[i] = max(memo[i], prices[j] - prices[i] + dfs(j + 2)) # sell at j that are buy at i
            return memo[i]       
        return dfs(0)
        