class Solution:
    def maxOperations(self, s: str) -> int:
        prev = 0
        res = 0
        for i in range(len(s)-2, -1, -1):
            prev = prev + (1 if s[i + 1] == "0" and s[i] == '1' else 0)
            if s[i] == '1':
                res += prev
        return res