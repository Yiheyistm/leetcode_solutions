class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')] # best sum with reminder 0, 1, 2

        for x in nums:
            prev = dp[:]
            for rem in range(3):
                new_rem = (rem + x) % 3
                dp[new_rem] = max(dp[new_rem], prev[rem] + x)

        return dp[0] # the only one which is divisible by 3
