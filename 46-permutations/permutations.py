class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permutation, bool_arr):
            nonlocal nums, res
            if len(permutation) == len(nums):
                res.append(permutation[:])
                
            for i in range(len(nums)):
                if not bool_arr[i]:
                    permutation.append(nums[i])
                    bool_arr[i] = True
                    backtrack(permutation, bool_arr)
                    permutation.pop()
                    bool_arr[i] = False

        res = []
        bool_arr = [False] * len(nums)
        backtrack([], bool_arr)
        return res

        