class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        for i in range(len(nums)):
            if nums[r] != 0 and nums[i] == 0:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1
            elif nums[r] == 0: r+=1

        w = r
        for i in range(r, len(nums)):
            if nums[w] != 1 and nums[i] == 1:
                nums[w], nums[i] = nums[i], nums[w]
                w += 1
            elif nums[w] == 1: w += 1

        