class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        n = len(nums)
        result = [-1] * (n - k + 1)
        l = 0

        for r in range(1, n):
            while l < r and nums[r] - nums[r -1] != 1:
                l += 1
            print(l, r)
            if r - l + 1 == k:
                result[l] = nums[r]
                l += 1
        return result
 
        
        