class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * (n + 1)
        def dp(h):
            if h >= n: return 0

            if memo[h] == -1:
                memo[h] = nums[h] + max(dp(h + 2), dp(h + 3))
            return memo[h]
        return max(dp(0), dp(1))

        