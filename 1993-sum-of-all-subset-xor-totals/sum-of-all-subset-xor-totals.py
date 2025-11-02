class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2**len(nums)):
            k = 0
            xor = 0
            while i > 0:
                if i & 1:
                    xor ^= nums[k]
                i >>= 1
                k += 1
            ans += xor
        return ans

        