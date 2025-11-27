class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_dict = defaultdict(int)
        pfx = list(accumulate(nums, initial=0))
        max_sum = -inf
        for i in range(len(pfx)):
            rem = i % k
            if rem in min_dict:
                max_sum = max(max_sum, pfx[i]-min_dict[rem])
                min_dict[rem] = min(min_dict[rem], pfx[i])
            else:
                min_dict[rem] = pfx[i]
        return max_sum
        
            

        