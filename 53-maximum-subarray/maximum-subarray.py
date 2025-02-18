class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            r_sum += nums[i]
            max_sum = max(r_sum, max_sum)
            if r_sum < 0 : r_sum = 0

        return max_sum
        