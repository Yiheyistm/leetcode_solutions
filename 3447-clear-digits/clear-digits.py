class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        i = 0
        while i < len(s):
            if s[i].isdigit():
                del s[i]
                del s[i - 1]
                i -= 2
            i += 1
        return ''.join(s)
        