class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev = 1
        cur = 1 if s[-1] != '0' else 0
        for i in range(n - 2, -1, -1):
            temp = 0
            if s[i] != '0':
                temp = cur + (prev if 1 <= int(s[i:i+2]) <= 26 else 0)
            prev = cur
            cur = temp
        return cur




        