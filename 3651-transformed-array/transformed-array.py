class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        res = []
        n = len(nums)
        return [nums[i] if num == 0 else nums[(num + i) % n] for i, num in enumerate(nums)]
        