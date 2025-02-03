class Solution(object):
    def twoSum(self, nums, target):
        num_set = set()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_set:
                return [nums.index(complement), i]
            num_set.add(nums[i])
        