class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target_sum = total_sum - x
        l = 0
        r_sum = 0
        max_len = -1
        for r in range(len(nums)):
            r_sum += nums[r]
            while l <= r and r_sum > target_sum:
                r_sum -= nums[l]
                l += 1
            if r_sum == target_sum:
                max_len = max(max_len, r - l + 1)
        return -1 if max_len == -1 else len(nums) - max_len

        