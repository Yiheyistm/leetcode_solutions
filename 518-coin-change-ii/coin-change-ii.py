class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        def dfs(i, rem):
            if rem == 0: return 1
            if i == len(coins): return 0

            if memo[i][rem] == -1:
                leave = dfs(i + 1, rem)
                take = 0
                if rem >= coins[i]:
                    take = dfs(i, rem - coins[i])
                memo[i][rem] = leave + take
            return memo[i][rem]
        return dfs(0, amount)


  
        