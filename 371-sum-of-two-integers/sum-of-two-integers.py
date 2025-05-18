class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a < 0:
            a = (1 << 32) + a
        if b < 0:
            b = (1 << 32) + b
        res = 0
        carry = 0
        k = 0
        while a > 0 or b > 0 or carry and k < 32:
            bit1 = 1 if a & 1 else 0
            bit2 = 1 if b & 1 else 0
            val, rem = divmod(bit1 + bit2 + carry, 2)
            res = (rem << k) | res
            carry = val
            a >>= 1
            b >>= 1
            k += 1

        if res.bit_length() >= 32: # if the res is negative
            res -= 1 << res.bit_length()

        return res
        
        