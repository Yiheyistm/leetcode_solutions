class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        max_sum = sum(nums)
        off_set = max_sum
        store = [[-1] * (2 * max_sum + 1) for _ in range(N)]

        def dfs(i, sm=0):
            if i == N:
                if sm == target:
                    return 1
                return 0
            if store[i][sm + off_set] == -1:
                store[i][sm + off_set] = dfs(i + 1, sm - nums[i]) + dfs(i + 1, sm + nums[i])

            return store[i][sm + off_set]
        return dfs(0 ,0)