class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        min_stack = []
        nums.append(0) # in case if the the stack are not empty at last 0 pops every remaining elements on the stack
        for num in nums:
            while min_stack and min_stack[-1] >= num:
                pop = min_stack.pop()
                if pop != num:
                    cnt += 1
            min_stack.append(num)

        return cnt

        