class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for rem in range(1, target +1):
            for num in nums:
                if rem - num >= 0:
                    dp[rem] += dp[rem - num]
                else:
                    break
        return dp[target]
