class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (r + l) // 2
            if mid * mid <= x:
                l = mid + 1
            else:
                r = mid -1
        return r
        