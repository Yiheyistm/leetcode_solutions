class Solution:
    def maxScore(self, s: str) -> int:
        no_1 = Counter(s)['1']
        n = len(s)
        num_map= {
            '0': 1,
            '1': 0}
        pfx_sum = 0
        mx_sum = 0
        for i, ch in enumerate(s):
            pfx_sum += num_map[ch]
            no_1 -= int(ch)
            if i == n-1  : break
            mx_sum = max(mx_sum, pfx_sum + no_1)
        return mx_sum

        