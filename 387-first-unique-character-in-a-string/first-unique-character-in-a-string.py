from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = -1
        count = Counter(s)
        for ch in range(len(s)):
            if count[s[ch]] == 1:
                unique = ch
                break
        return unique

        