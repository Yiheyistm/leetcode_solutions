class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2: return False
        
        memo = {}
        n = len(nums)
        def dp(i, sm):
            if i == n: 
                return sm == 0
            if sm - nums[i] < 0:
                 return dp(i + 1, sm)
            if (i, sm) not in memo:
                for j in range(i, n):
                    memo[(j, sm)] = dp(j + 1, sm - nums[j])
                    if memo[(j,sm)]: return True
            return memo[(i, sm)]
        
        return dp(0, sum_ // 2)


        