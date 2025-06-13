class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        new_nums1 = []
        for n1 in nums1:
            for n2 in nums2:
                new_nums1.append(n1 + n2)

        new_nums2 = []
        for n1 in nums3:
            for n2 in nums4:
                new_nums2.append(n1 + n2)

        count = 0
        counter = Counter(new_nums1)
        for n1 in new_nums2:
            diff = 0 - n1
            if diff in counter:
                count += counter[diff]
        return count