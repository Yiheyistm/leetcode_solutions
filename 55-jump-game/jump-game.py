class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx_jump = 0

        for i in range(len(nums)):
            mx_jump = max(mx_jump, nums[i] + i)
            if mx_jump == i and i != len(nums) -1:
                return False
        return True
        