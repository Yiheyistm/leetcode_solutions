class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach = 0
        needed = 0
        i = 0
        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                reach += nums[i]
                i += 1
            else:
                needed += 1
                reach += (reach + 1)
        return needed

