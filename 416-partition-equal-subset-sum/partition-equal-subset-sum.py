class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        n = len(nums)
        if sum_ % 2: return False
        
        target = sum_ // 2
        dp = [False] * (target + 1)
        dp[0] = True
        dp2 = [False] * (target + 1)
        dp2[0] = True

        for i in range(n -1, -1, -1):
           for sm in range(target + 1):
                if sm >= nums[i]:
                    dp[sm] |= dp2[sm - nums[i]]
                dp[sm] |= dp2[sm]

           dp2 = dp[:]
        return dp[target]


        