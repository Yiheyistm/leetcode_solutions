class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        n = len(nums)
        if sum_ % 2: return False
        
        target = sum_ // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True
        for i in range(n -1, -1, -1):
           for sm in range(target + 1):
                leave = dp[i + 1][sm]
                take = False
                if sm >= nums[i]:
                    take = dp[i + 1][sm - nums[i]]
                dp[i][sm] = take or leave
        return dp[0][target]


        