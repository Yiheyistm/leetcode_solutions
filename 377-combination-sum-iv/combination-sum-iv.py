class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        memo = [-1] * (target + 1)
        def dfs(rem):
            if rem == 0: return 1
            if rem < 0:
                return 0
            if memo[rem] == -1:
                memo[rem] = 0
                for j in range(N):
                    memo[rem] += dfs(rem - nums[j])
            return memo[rem]
        return dfs(target)
