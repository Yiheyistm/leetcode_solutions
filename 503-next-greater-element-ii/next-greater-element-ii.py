class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = [-1] * n
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                lst[stack.pop()] = num
            stack.append(i)

        ln = stack[0]
        for i in range(ln + 1):
            if len(stack) == 1:
                break
            while stack and nums[stack[-1]] < nums[i]:
                lst[stack.pop()] = nums[i]

        return lst
