class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        n = len(nums)
        if sum_ % 2: return False
        
        target = sum_ // 2
        memo = [[-1] * (target + 1) for _ in range(n + 1)]
        def dp(i, sm):
            if sm == 0:
                return True
            if i == n or sm < 0:
                return False
            if memo[i][sm] == -1:
                take = dp(i + 1, sm - nums[i])
                leave = dp(i + 1, sm)
                memo[i][sm] = take or leave
            return memo[i][sm]
        
        return dp(0, target)


        