class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        effective_buy = prices[0]
        for p in prices:
            profit = max(profit, p - effective_buy - fee)
            effective_buy = min(effective_buy, p - profit)
        return profit
        