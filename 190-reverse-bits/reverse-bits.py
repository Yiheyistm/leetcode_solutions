class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]
        if n.bit_length() < 32:
            num = '0'*(32 - n.bit_length()) + num
        return int(num[::-1], 2)
        