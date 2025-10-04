class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)

        dp = [1]*N
        for p in range(N):
            for c in range(p):
                if nums[c] < nums[p]:
                    dp[p] = max(dp[p], 1 + dp[c])

        return max(dp)
