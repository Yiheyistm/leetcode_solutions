class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = float('inf'), 0
        profit = 0
        for p in prices:
            sell = max(sell, p)
            if p < buy:
                sell = p
                buy = p
            profit = max(profit, sell - buy)
        return profit
        