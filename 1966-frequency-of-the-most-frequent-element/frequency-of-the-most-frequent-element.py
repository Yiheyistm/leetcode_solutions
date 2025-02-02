class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        max_freq = 1
        total = 0

        for right in range(len(nums)):
            total += nums[right]
            diff = right - left + 1

            while nums[right] * diff > total + k:
                total -= nums[left]
                left += 1
                diff -= left
            max_freq = max(max_freq, diff)

        return max_freq


        