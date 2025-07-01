class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        h = len(nums)
        while l + 1 < h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid
            else:
                l = mid
        return h
        