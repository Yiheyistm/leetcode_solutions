class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        unque = len(set(nums))
        no_sub = 0
        l = 0
        for r in range(n):
            cnt[nums[r]] += 1
            while l <= r and len(cnt) >= unque:
                cnt[nums[l]] -= 1
                if not cnt[nums[l]]:
                    del cnt[nums[l]]
                l += 1
            no_sub += r - l + 1
        return (n * (n + 1) // 2) - no_sub

        