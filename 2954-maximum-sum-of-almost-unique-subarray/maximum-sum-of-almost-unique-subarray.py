class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        unq = defaultdict(int)
        mx = rsum = 0
        left = 0
        for i in range(len(nums)):
            rsum += nums[i]
            unq[nums[i]] += 1
            if i - left + 1 == k:
                if len(unq) >= m:
                    mx = max(mx, rsum)
                rsum -= nums[left]
                unq[nums[left]] -= 1
                if not unq[nums[left]]: del unq[nums[left]]
                left += 1
        return mx
        