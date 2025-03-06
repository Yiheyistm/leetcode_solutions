class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Using monotonic queue we can track the largest and the smallest in the window
        maxStk = deque() # for decreasing stack the largest is on index 0 (monotonic decreasing)
        minStk = deque() # for increasing stack the the smallest is on index 0 (monotonic increasing)
        longest = 0
        l = 0
        for r, n in enumerate(nums):
            # remove element on the decreasing stack until the largest element left which is greater than current
            while maxStk and maxStk[-1] < n:
                maxStk.pop()
            maxStk.append(n)

            # remove element on the increasing stack until the smalles element left which is less than current
            while minStk and minStk[-1] > n:
                minStk.pop()
            minStk.append(n)

            # shrink window if max - min exceeds limit
            while maxStk[0] - minStk[0] > limit:
                if maxStk[0] == nums[l]:
                    maxStk.popleft()
                if minStk[0] == nums[l]:
                    minStk.popleft()
                l += 1
            longest = max(longest, r - l + 1)
        return longest


            

        