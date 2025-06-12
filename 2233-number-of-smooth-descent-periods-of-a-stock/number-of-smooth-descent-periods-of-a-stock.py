class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        sub_arr = 1
        l = 0
        for r in range(1, len(prices)):
            if prices[r - 1] - prices[r] != 1:
                l = r
            sub_arr += r - l + 1
        return sub_arr
        