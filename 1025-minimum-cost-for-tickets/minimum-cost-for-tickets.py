class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 500

        for day in range(365, -1, -1):
            d1 = bisect_left(days, day + 1)
            d7 = bisect_left(days, day + 7)
            d30 = bisect_left(days, day + 30)
            
            dp[day] = min(
                costs[0] + (dp[days[d1]] if d1 < len(days) else 0),
                costs[1] + (dp[days[d7]] if d7 < len(days) else 0),
                costs[2] + (dp[days[d30]] if d30 < len(days) else 0)
            )
        
        return dp[days[0]]

        @cache
        def dfs(day):
            if day >= days[-1]:
                return 0 if day > days[-1] else min(costs)
            
            d1 = bisect_left(days, day + 1)
            d7 = bisect_left(days, day + 7)
            d30 = bisect_left(days, day + 30)
            
            return min(
                costs[0] + (dfs(days[d1]) if d1 < len(days) else 0),
                costs[1] + (dfs(days[d7]) if d7 < len(days) else 0),
                costs[2] + (dfs(days[d30]) if d30 < len(days) else 0)
            )

        return dfs(days[0])