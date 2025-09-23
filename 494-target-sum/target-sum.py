class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        store = [[-1] * 1001 for _ in range(N)]

        def dfs(i, sm=0):
            if i == N:
                if sm == target:
                    return 1
                return 0
            if store[i][sm] == -1:
                store[i][sm] = dfs(i + 1, sm - nums[i]) + dfs(i + 1, sm + nums[i])

            return store[i][sm]
        return dfs(0 ,0)