class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numIdx = defaultdict(lambda: -1)
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack:
                numIdx[nums2[i]] = stack[-1]
                
            stack.append(nums2[i])
                
        return [numIdx[n] for n in nums1]
        