class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, rem):
            if rem == 0: return 1
            if i == len(coins): return 0

            leave = dfs(i + 1, rem)
            take = 0
            if rem >= coins[i]:
                take = dfs(i, rem - coins[i])
            return leave + take
        return dfs(0, amount)


  
        