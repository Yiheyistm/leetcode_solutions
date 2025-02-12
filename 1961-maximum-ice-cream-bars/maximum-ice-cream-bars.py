class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_num = max(costs)
        count = [0] * (max_num + 1)
        for cost in costs:
            count[cost] += 1
        target = 0
        for i, val in enumerate(count):
            for j in range(val):
                costs[target] = i
                target += 1
        
        no_shop = 0
        for coin in costs:
            if coin > coins:
                break
            coins -= coin
            no_shop += 1
        return no_shop
        

        