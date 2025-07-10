class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = 1
        dup = 0
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                cnt += dup
                dup = 0
            else:
                dup += 1

        if dup:
            cnt += dup
        return cnt
        