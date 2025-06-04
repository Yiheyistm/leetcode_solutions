class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        return nums[-1][1] if nums[-1][0] >= 2 * nums[-2][0] else -1
        