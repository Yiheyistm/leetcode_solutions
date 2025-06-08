class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_ = max(nums)
        cnt = 0
        no_sub = 0
        l = 0
        for r in range(n):
            cnt += 1 if nums[r] == max_ else 0
            while l <= r and cnt >= k:
                cnt -= 1 if nums[l] == max_ else 0
                l += 1
            no_sub += r - l + 1
        
        return (n * (n + 1) // 2) - no_sub
        