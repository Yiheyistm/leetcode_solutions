class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums += nums
        n = len(nums)
        lst = [-1] * n
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                lst[stack.pop()] = num
            stack.append(i)

        return lst[:n//2]
