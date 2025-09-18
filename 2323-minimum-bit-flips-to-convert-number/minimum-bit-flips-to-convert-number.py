class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_ = start ^ goal
        cnt = 0
        while xor_:
            if xor_ & 1:
                cnt += 1
            xor_ >>= 1
        return cnt
        