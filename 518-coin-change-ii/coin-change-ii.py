class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for rem in range(amount + 1):
                res = dp[i + 1][rem]
                if rem >= coins[i]:
                    res += dp[i][rem - coins[i]]
                dp[i][rem] = res
        return dp[0][amount]
