class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prfx_max =  [0]
        prev_mn, prev_mx = prices[0], prices[0] # min, max
        for i in range(1, len(prices)):
            mx = max(prices[i], prev_mx)
            if prices[i] < prev_mn:
                prev_mn,prev_mx = prices[i], prices[i]
                prfx_max.append(prfx_max[i -1])

            else:
                prev_mx = mx
                prfx_max.append(max(prfx_max[i - 1], prev_mx - prev_mn))
        
        sfx_max = [0] * len(prices)
        prev_mn, prev_mx = prices[-1], prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            mn = min(prices[i], prev_mn)
            if prices[i] > prev_mx:
                prev_mn, prev_mx = (prices[i], prices[i])
                sfx_max[i] = sfx_max[i + 1]
            else:
               prev_mn = mn
               sfx_max[i] = max(sfx_max[i +1], prev_mx - mn)

        ans = 0
        for i in range(len(prices)-1):
            lef = prfx_max[i]
            right = sfx_max[i]
            ans = max(ans, lef + right)
        return ans



        