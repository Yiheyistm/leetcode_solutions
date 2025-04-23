class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        r_sum = sum(nums[:k])
        d = Counter(nums[:k])
        max_sum = r_sum if len(d) == k else 0
        for i in range(k, len(nums)):
            d[nums[i-k]] -= 1
            if not d[nums[i-k]]: del d[nums[i-k]]
            r_sum += nums[i] - nums[i - k]
            d[nums[i]] += 1

            if len(d) == k and max_sum < r_sum:
                max_sum = r_sum

        return max_sum

