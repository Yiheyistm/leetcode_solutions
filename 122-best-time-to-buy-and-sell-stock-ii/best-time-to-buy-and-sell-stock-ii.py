class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            prof = prices[i] - prices[i -1]
            ans += prof if prof > 0 else 0
        return ans

        