class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev = 1
        cur = 1 if s[0] != '0' else 0
        for i in range(1, n):
            temp = 0
            if s[i] != '0':
                temp = cur
            if  '1' <= s[i-1:i+1] <= '26':
                temp += prev
            prev = cur
            cur = temp
        return cur




        