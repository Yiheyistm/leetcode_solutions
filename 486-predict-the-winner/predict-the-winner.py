class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * (n) for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for d in range(1, n):
            for l in range(n - d):
                r = l + d
                dp[l][r] = max(nums[l] - dp[l + 1][r], nums[r] - dp[l][r - 1])
            
        return dp[0][n-1] >= 0
        