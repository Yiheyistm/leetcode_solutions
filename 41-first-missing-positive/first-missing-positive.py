class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            x = nums[i]
            if 1 <= x <= n and x != nums[x - 1]:
                nums[i], nums[x - 1] = nums[x -1], nums[i]
            else:
                i += 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1

        