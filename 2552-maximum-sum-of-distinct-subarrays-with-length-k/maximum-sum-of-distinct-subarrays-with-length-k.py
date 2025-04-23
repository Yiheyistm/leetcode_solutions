class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        r_sum = sum(nums[:k])
        freq = Counter(nums[:k])
        max_sum = r_sum if len(freq) == k else 0
        len_sub = len(freq)
        for i in range(k, len(nums)):
            freq[nums[i-k]] -= 1
            if not freq[nums[i-k]]: 
                len_sub -= 1
                del freq[nums[i-k]]

            len_sub += 1 if nums[i] not in freq else 0
            r_sum += nums[i] - nums[i - k]
            freq[nums[i]] += 1
            if len_sub == k and max_sum < r_sum:
                max_sum = r_sum

        return max_sum

