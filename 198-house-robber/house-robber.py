class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        prev_prev = nums[0]
        prev = max(nums[1], prev_prev)
        for h in range(2, n):
                temp = max(prev_prev + nums[h], prev)
                prev_prev = prev
                prev = temp
        return prev

        