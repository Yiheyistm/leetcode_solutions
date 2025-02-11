class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        l = len(part)
        while True:
            t = s.find(part)
            if t == -1:
                break
            s = s[:t] + s[t+l:]
        return s
        