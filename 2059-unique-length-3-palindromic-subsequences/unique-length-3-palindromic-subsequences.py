class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counter = Counter(s)
        pairs = defaultdict(list) # ch -> [first_index, last_index]
        for i, ch in enumerate(s):
            if ch in pairs:
                pairs[ch][1] = i
            else:
                pairs[ch] = [i, inf]

        cnt = 0
        for ch in set(s):
            f_idx, l_idx = pairs[ch]
            if l_idx == inf: continue
            cnt += len(set(s[f_idx + 1: l_idx]))
        return cnt
        