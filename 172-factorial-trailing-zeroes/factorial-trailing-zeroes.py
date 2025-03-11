class Solution:
    def trailingZeroes(self, n: int) -> int:
        def recur(n):
            if n == 0:
                return 0
            y = n // 5
            return y + recur(y)
        x = recur(n)
        return x
        
        