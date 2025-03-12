class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = [] # [nums, index]
        pfx = list(accumulate(nums, initial = 0))
        MOD = 10 ** 9 + 7
        res = 0
        for i, num in enumerate(nums):
            newIdx = i
            while stack and stack[-1][0] >= num:
                val, idx = stack.pop()
                res = max(res, val * (pfx[i] - pfx[idx]))
                newIdx = idx
            stack.append([num, newIdx])
        # the numbers left from the stack are nums that are smallest of the sum array from idx to last element
        for num, idx in stack:
            res = max(res, num * (pfx[-1] - pfx[idx]))
        
        return res % MOD
        