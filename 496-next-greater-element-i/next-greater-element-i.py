class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numIdx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        for i, n in enumerate(nums2):
            if n in numIdx:
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > n:
                        idx = numIdx[n]
                        res[idx] = nums2[j]
                        break
        return res
        