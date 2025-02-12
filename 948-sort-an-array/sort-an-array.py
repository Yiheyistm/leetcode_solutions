class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num = abs(min(nums))
        max_num = max(nums)
        count = [0] * (max_num + min_num + 1)
        for num in nums:
            count[num + min_num] += 1

        target = 0
        for i, val in enumerate(count):
            for j in range(val):
                nums[target] = i - abs(min_num)
                target += 1
        return nums
        