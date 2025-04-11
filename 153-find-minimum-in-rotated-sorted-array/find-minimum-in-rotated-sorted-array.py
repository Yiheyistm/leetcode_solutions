class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = -1
        h = len(nums) -1
        while l + 1 < h:
            m = (l + h) // 2
            if nums[m] < nums[h]:
                h = m
            else: l = m
        return nums[h]
        