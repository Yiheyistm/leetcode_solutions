class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for cur_num in reversed(arr):
                dp[cur_num] = dp[cur_num + difference] + 1
        return max(dp.values())
