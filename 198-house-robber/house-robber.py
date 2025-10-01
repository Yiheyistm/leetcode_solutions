class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [-1] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        for h in range(2, n):
                dp[h] = max(dp[h - 2] + nums[h], dp[h - 1])
        return dp[-1]

        