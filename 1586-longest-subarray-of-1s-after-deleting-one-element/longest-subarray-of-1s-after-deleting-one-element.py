class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zero_cnt = 0
        max_len = 0
        for r in range(len(nums)):
            zero_cnt += 1 if nums[r] == 0 else 0
            while l <= r and zero_cnt > 1:
                zero_cnt -= 1 if nums[l] == 0 else 0
                l += 1
            max_len  = max(r - l, max_len)
        return max_len
        