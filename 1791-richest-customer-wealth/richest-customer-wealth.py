class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(len(accounts)):
            t = sum(accounts[i])
            wealth = max(wealth, t)

        return wealth