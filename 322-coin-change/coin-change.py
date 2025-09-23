class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        store = [[-1] * (amount + 1) for _ in range(n)]
        def dfs(i, rem):
            if rem == 0:
                return 0
            if i == n or rem < 0:
                return float("inf")

            if store[i][rem] == -1:
                skip = dfs(i + 1, rem)
                take = float('inf')
                if rem >= coins[i]:
                    take = (dfs(i, rem - coins[i]))
                    if take != float('inf'):
                        take += 1
                store[i][rem]  = min(skip, take)
            return store[i][rem]

        res = dfs(0, amount)
        return res if res != float('inf') else -1
            
        