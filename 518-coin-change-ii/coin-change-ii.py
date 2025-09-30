class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp2 = [0] * (amount + 1)
        dp[0] = 1
        dp2[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for rem in range(amount + 1):
                res = dp2[rem]
                if rem >= coins[i]:
                    res += dp[rem - coins[i]]
                dp[rem] = res
            dp2 = dp[:]
            
        return dp[amount]
