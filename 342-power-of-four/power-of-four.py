class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def checker(n):
            if n == 0:return False
            if n == 1:return True
            return checker(n/4)
        return checker(n)

        