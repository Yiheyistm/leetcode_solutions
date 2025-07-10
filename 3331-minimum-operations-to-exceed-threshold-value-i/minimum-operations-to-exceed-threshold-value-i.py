class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = -1
        h = len(nums) - 1
        while l + 1 < h:
            mid  = (l + h) // 2
            if nums[mid] >= k:
                h = mid
            else: l = mid
        return h
        