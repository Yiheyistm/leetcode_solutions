class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checker(mid):
            mx = 0
            cnt = 1
            prev = 0

            for p in nums:
                prev += p
                if prev > mid:
                    cnt += 1
                    mx = max(mx, prev - p)
                    prev = p
            mx = max(mx, prev)
            return cnt <= k, mx

        l = -1
        h = sum(nums) + 1
        ans = float('inf')
        while l + 1 < h:
            md = (l + h) // 2
            isValid, mx = checker(md)
            if isValid:
                ans = min(ans, mx)
                h = md
            else: l = md
        return ans

        