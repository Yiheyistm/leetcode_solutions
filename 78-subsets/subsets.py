class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx, subset):
            nonlocal nums,res
            if idx <= len(nums):
                res.append(subset[:])
            if idx > len(nums):
                return

            for j in range(idx, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
        backtrack(0, [])
        return res
        

        