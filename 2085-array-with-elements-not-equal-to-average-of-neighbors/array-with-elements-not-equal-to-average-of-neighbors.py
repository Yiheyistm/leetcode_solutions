class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        median = len(nums) // 2
        i = 0
        while (i + median + 1) < len(nums):
            ans.append(nums[i])
            ans.append(nums[i + median +1])
            i += 1
        if len(nums) % 2 == 1:
            ans.append(nums[median])
        else:
            ans.append(nums[i])
            ans.append(nums[median])
        return ans
        