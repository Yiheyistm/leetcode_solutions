class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total_subarray = n * (n + 1) // 2
        not_good_subarray = 0
        freq = defaultdict(int)
        pair_cnt = 0
        l = 0
        for r in range(n):
                freq[nums[r]] += 1
                v = freq[nums[r]]
                pair_cnt += (v - 1)
                while pair_cnt >= k:
                    pair_cnt -= (freq[nums[l]] - 1)
                    freq[nums[l]] -= 1
                    l += 1
                not_good_subarray += r - l + 1

        return total_subarray - not_good_subarray

        