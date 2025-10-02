class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        buy_price = prices[0]
        for p in prices:
            if p - buy_price > fee:
                profit += p - buy_price - fee
                buy_price = p - fee
            buy_price = min(buy_price, p)
        return profit
        