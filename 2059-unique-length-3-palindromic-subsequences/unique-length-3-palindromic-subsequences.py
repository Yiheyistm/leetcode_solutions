class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counter = Counter(s)
        pairs = defaultdict(list) # ch -> [first_index, last_index]
        for i, ch in enumerate(s):
            if ch in pairs:
                pairs[ch][1] = i
            else:
                pairs[ch] = [i, inf]

        unique = set()
        pfx = []
        r_sum = 0
        for ch in s:
            if ch not in unique:
                r_sum += 1
            unique.add(ch)
            pfx.append(r_sum)

        cnt = 0
        for ch in set(s):
            f_idx, l_idx = pairs[ch]
            if l_idx == inf or f_idx + 1 == l_idx: continue
            cnt += len(set(s[f_idx + 1: l_idx]))
        return cnt
        