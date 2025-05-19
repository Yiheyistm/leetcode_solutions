class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0:
            a = a + (1 << 32)
        if b < 0:
            b = b + (1 << 32)

        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
            b &= 0xFFFFFFFF

        if a >= (1 << 31):
            a -= (1 << 32)

        return a
        
        