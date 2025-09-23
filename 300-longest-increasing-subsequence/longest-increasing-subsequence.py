class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        def dp(i):
            if memo[i] == -1:
                memo[i] = 1
                for j in range(i+1, n):
                    if nums[i] < nums[j]:
                        memo[i] = max(memo[i], 1 + dp(j))
            return memo[i] 
        
        max_len = 0
        for i in range(n):
            max_len = max(max_len, dp(i))
        return max_len
        