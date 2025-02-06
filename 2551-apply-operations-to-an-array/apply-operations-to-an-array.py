class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]
                nums[i + 1] = 0
        l = r = 0
        while r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            if nums[l] != 0 and nums[r] == 0:
                l = r
            r += 1
        return nums
