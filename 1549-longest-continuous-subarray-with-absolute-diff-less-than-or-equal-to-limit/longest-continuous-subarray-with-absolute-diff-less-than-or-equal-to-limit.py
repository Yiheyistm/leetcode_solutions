class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxStk = deque()
        minStk = deque()
        longest = 0
        l = 0
        for r, n in enumerate(nums):
            while maxStk and maxStk[-1][0] < n:
                maxStk.pop()
            maxStk.append((n, r))
            while minStk and minStk[-1][0] > n:
                minStk.pop()
            minStk.append((n, r))
            while maxStk[0][0] - minStk[0][0] > limit:
                if maxStk[0][1] < minStk[0][1]:
                    l = maxStk[0][1] + 1
                    maxStk.popleft()
                else:
                    l = minStk[0][1] + 1
                    minStk.popleft()

            longest = max(longest, r - l + 1)
            
        return longest


            

        