class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_pro = [nums[0]]
        for i in range(1, len(nums)):
            prefix_pro.append(prefix_pro[-1] * nums[i])

        suffix_pro = [1] * len(nums)
        suffix_pro[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix_pro[i] = (suffix_pro[i + 1] * nums[i])
            
        for i in range(len(nums)):
            if i == 0:
                nums[i] = suffix_pro[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix_pro[i - 1]
            else:
                nums[i] = prefix_pro[i - 1] * suffix_pro[i + 1]
        return nums
        