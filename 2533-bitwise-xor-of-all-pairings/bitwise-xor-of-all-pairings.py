class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        ans = 0
        if len2 & 1:
            for v in nums1:
                ans ^= v
        if len1 & 1:
            for v in nums2:
                ans ^= v
        return ans
            
        
        