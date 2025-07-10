class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        line_sweep = [0] * (len(nums) + 1)
        for a,b in queries:
            line_sweep[a] += 1
            line_sweep[b + 1] -= 1
        pfx = list(accumulate(line_sweep))
        for i in range(len(nums)):
            if nums[i] - pfx[i] > 0:
                return False
        return True
        