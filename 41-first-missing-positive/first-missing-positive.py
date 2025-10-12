class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        miss_num = 1
        for num in nums:
            if num > miss_num:
                break
            if num == miss_num:
                miss_num += 1

        return miss_num

        