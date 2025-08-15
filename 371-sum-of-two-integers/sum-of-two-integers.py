class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        ans = 0
        for i in range(32):
            al, bl = (a & 1), (b & 1)
            cur = al ^ bl ^ c
            c = (al & bl) | (al & c) | (bl & c)
            ans |= cur << i
            a >>= 1
            b >>= 1

        if ans & (1 << 31): # if the ans is negative the bitlength is above 31
            ans -= 1 << 32
        
        return ans

        