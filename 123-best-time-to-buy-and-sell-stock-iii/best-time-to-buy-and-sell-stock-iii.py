class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prfx =  []
        prfx.append((prices[0], prices[0])) # min, max
        for i in range(1, len(prices)):
            mx = max(prices[i], prfx[i - 1][1])
            if prices[i] < prfx[i - 1][0]:
                prfx.append((prices[i], prices[i]))

            else:
                prfx.append((prfx[i-1][0], mx))
        

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
            lef = prfx[i][1] - prfx[i][0]
            right = sfx_max[i]
            ans = max(ans, lef + right)
        return ans


        # heap = [0] * 2
        # buy_p = prices[0]
        # for i in range(len(prices)-1):
        #     if prices[i + 1] < prices[i] and buy_p < prices[i]:
        #         heappushpop(heap, prices[i] - buy_p)
        #         buy_p = prices[i + 1]
        #     buy_p = min(buy_p, prices[i])

        # heappushpop(heap, prices[-1] - buy_p)
        # return heappop(heap) + heappop(heap)




        