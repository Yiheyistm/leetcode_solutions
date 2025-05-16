class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        prev = nums[0]
        or_ = nums[0]
        max_len = 1
        for i in range(1, len(nums)):
            while l < i and (nums[l] & nums[i] != 0 or or_ & nums[i] != 0 or prev & nums[i]):
                max_len = max(max_len, i - l)
                or_ ^= nums[l]
                l += 1

            or_ |= nums[i]
            prev = nums[i]

        max_len = max(max_len, len(nums) - l)
        return max_len

        