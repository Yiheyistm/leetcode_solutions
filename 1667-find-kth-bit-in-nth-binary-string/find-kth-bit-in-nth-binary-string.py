class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        lenStr = pow(2, n) - 1 # lenght of binary
        flip = False
        while n > 1:
            mid = lenStr // 2 + 1 #because of 1 is append in the middle
            if mid == k:
                return '1' if not flip else '0'
            if k < mid:
                lenStr = mid - 1
            else:
                k = lenStr - k + 1
                lenStr = lenStr // 2
                flip = not flip
            n -= 1
        return '0' if not flip else '1'