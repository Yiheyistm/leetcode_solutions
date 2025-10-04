class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        uniques = sorted(cnt.keys())
        N = len(uniques)
        dp = [0] * (N + 1)
        for i in range(N-1, -1, -1):
            earn = uniques[i] * cnt[uniques[i]]
            if  i + 1 < N and (uniques[i+1] - uniques[i] == 1):
                dp[i] = max(earn + dp[i+2], dp[i+1])
            else:
                dp[i] = earn + dp[i + 1]
        return dp[0]

           

        