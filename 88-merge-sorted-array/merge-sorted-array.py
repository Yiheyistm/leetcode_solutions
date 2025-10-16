class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       j = 0
       for i in range(len(nums1)):
        if nums1[i] == 0 and i >= m and nums2:
            nums1[i] = heappop(nums2)
        elif nums2 and nums1[i] > nums2[0]:
            heappush(nums2, nums1[i])
            nums1[i] = heappop(nums2)
    
        