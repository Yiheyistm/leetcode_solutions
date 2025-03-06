class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numIdx = defaultdict(lambda: -1)
        stack = []
        for i, n in enumerate(nums2):
            while stack and stack[-1] < n:
                numIdx[stack.pop()] = n
            stack.append(n)
                
        return [numIdx[n] for n in nums1]
        