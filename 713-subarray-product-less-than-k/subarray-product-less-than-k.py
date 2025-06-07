class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        no_sub = 0
        prod = 1
        l = 0
        for i in range(len(nums)):
            prod *= nums[i]
            while l <= i and prod >= k:
                prod /= nums[l]
                l += 1
            no_sub += i - l + 1
        return no_sub
        