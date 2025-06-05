class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_, min_ = max(nums), min(nums)
        mxlc = -1
        mnlc = -1
        
        for i in range(n):
            if max_ == nums[i]:
                mxlc = i
            if min_ == nums[i]:
                mnlc = i

        l = min(mnlc, mxlc)
        r = max(mnlc, mxlc)
        return min (r+1, n - l,(l + 1) + (n - r) )


        
    
        