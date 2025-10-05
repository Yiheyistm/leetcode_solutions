class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def dfs(day):
            if day >= n-1:
                return 0
            return max(0, (prices[day + 1] - prices[day])) + dfs(day + 1)
        return dfs(0)
        