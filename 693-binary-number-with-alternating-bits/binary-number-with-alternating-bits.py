class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ (n >> 1)
        return True if n == ((1 << n.bit_length()) -1) else False
        