class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_xor = 0
        idx_xor = 0
        for i in range(len(nums)):
            num_xor ^= nums[i]
            idx_xor ^= (i + 1)
        return num_xor ^ idx_xor

        