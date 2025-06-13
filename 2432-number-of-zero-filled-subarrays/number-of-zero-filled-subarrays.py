class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        r_sum = 0
        l = 0
        sub_arr = 0
        for r in range(len(nums)):
            r_sum += nums[r]
            while l <= r and r_sum != 0:
                r_sum -= nums[l]
                l += 1
            sub_arr += r - l + 1
        return sub_arr
        