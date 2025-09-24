class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        store = [float('inf')] * (amount + 1)
        store[0] = 0
        for coin in coins:
            for amt in range(coin, amount +1):
                store[amt] = min(store[amt], store[amt - coin] + 1)

        res = store[amount]
        return res if res != float('inf') else -1
            
        