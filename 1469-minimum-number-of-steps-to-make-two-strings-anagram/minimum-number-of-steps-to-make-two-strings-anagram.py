from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_t = Counter(t)
        counter_s = Counter(s)
        change = 0

        for ch in counter_t:
            if ch in counter_s:
                diff = counter_t[ch] - counter_s[ch]
                if diff < 0:
                    continue
                change += diff
            else:
                change += counter_t[ch]
        return change
