class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * (n + 1)
        def dp(h):
            if h == 0: return nums[h]
            if h == 1:
                return max(nums[0],nums[1])

            if memo[h] == -1:
                memo[h] = max(dp(h - 2) + nums[h], dp(h - 1))
            return memo[h]

        return dp(n - 1)

        