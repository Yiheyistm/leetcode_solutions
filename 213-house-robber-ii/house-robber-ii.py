class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1: return nums[0]
        memo = [-1] * len(nums)
        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if memo[i] == -1:
                memo[i] = max(dfs(i-1), dfs(i - 2) + nums[i])
            return memo[i]
        first =  dfs(len(nums)-2)

        memo2 = [-1] * len(nums)
        def dfs2(i):
            if i == 1:
                return nums[1]
            if i == 2:
                return max(nums[1], nums[2])
            if memo2[i] == -1:
                memo2[i] = max(dfs2(i-1), dfs2(i - 2) + nums[i])
            return memo2[i]
        sec =  dfs2(len(nums)-1)

        return max(first, sec)

        