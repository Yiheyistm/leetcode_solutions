class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pfx = list(accumulate(nums, initial = 0))
        min_pfx = dict()

        mx = float('-inf')
        for i,v in enumerate(nums):
            for diff in (v + k, v - k):
                if diff in min_pfx:
                    mx = max(mx, pfx[i + 1] - min_pfx[diff])
            if v not in min_pfx:
                min_pfx[v] = pfx[i]
            else: min_pfx[v] = min(min_pfx[v], pfx[i]) # min pfx gives max subarray sum

        return 0 if mx == float('-inf') else mx



        