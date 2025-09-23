class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * n for _ in range(n)]
        def dp(i, last):
            if i >= n:
                return 0
            if memo[i][last] == -1:
                exclude = dp(i + 1, last)

                include = 0
                if last == -1 or nums[last] < nums[i]:
                    include = 1 + dp(i + 1, i)
                memo[i][last] = max(exclude, include)
            return memo[i][last] 
        return dp(0, -1)
        