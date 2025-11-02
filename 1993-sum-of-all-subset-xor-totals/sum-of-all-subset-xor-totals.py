class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums) + 1):
            ls = combinations(nums, i)
            for l in ls:
                ans += reduce(xor, l)
        return ans
        