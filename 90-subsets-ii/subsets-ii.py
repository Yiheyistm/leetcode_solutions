class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        my_set = set()
        def backtrack(idx, subset):
            nonlocal nums,res, my_set
            if idx <= len(nums):
                res.append(subset[:])
            if idx > len(nums):
                return

            for j in range(idx, len(nums)):
                if tuple(subset + [nums[j]]) in my_set: continue
                subset.append(nums[j])
                my_set.add(tuple(subset))
                backtrack(j + 1, subset)
                subset.pop()
        backtrack(0, [])
        return res
        