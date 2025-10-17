class Solution:
    def reverse(self, x: int) -> int:
        mx = 2147483647
        mn = -2147483648

        res = 0
        isNeg = -1 if x < 0 else 1
        x = x * isNeg
        while x > 0:
            last = x % 10
            res = (res * 10) + last
            x //= 10
            
        res = res * isNeg
        if res > mx or res < mn:
            return 0
        
        return res