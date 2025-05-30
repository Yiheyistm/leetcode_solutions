class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        alphWithValue = {chr(i + 96): i for i in range(1,27)}
        for i, ch in enumerate(chars):
            alphWithValue[ch] = vals[i]

        max_sum = 0
        sum = 0
        for ch in s:
            sum += alphWithValue[ch]
            max_sum = max(sum, max_sum)
            if sum < 0:
                sum = 0
        return max_sum

        