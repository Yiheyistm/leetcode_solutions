class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def calc(arr):
            prev1, prev2 = 0, 0
            for num in arr:
                prev1, prev2 = max(prev1, prev2 + num), prev1
            return prev1
        return max(calc(nums[1:]), calc(nums[:-1]))

        