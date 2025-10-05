# At any given index i there are one of the 3 states:
# hold: max profit when holding a stock (in hand stock)
# sold: max profit after selling a stock
# rest: max profit in cooldown or idle state
# Rule of state:
# When you buy, you transition from rest → hold.
# When you sell, you transition from hold → sold.
# # After selling, you cool down (sold → rest).
# State Transition:
# hold: you can transite to hold state by either keeping holding or buy stock
# rest: you can transite to rest state by either keeping rest or sell
# sell: you can transite to sell by selling the stock in hand
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0] # let's assume you bought a stock and you profit decrease by prices[0]
        sell = 0 
        rest = 0
        for price in prices[1:]: # since you bought at index 0 afte it you can sell it
            prev_sold = sell
            sell = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)

        return max(sell, rest) # we know that sell is profitable than hold
        