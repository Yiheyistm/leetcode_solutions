class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sum = 0
        l = 0
        no_sub = 0
        for r in range(len(nums)):
            sum += nums[r]
            temp_len = r - l + 1
            while l <= r and (temp_len) * (sum) >= k:
                sum -= nums[l]
                temp_len -= 1
                l += 1
            no_sub += r - l + 1
        return no_sub
        