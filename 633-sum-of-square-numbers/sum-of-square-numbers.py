class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        mid = int(math.sqrt(c))
        left = 0
        while left <= mid:
            sm = left ** 2 + mid ** 2
            if sm == c:
                return True
            elif sm > c:
                mid -= 1
            else:
                left += 1
        return False