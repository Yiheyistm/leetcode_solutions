class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def pow(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n not in memo:
                half_1 = pow(x, n // 2)
                half_2 = pow(x, n - (n // 2))
                memo[n] =  half_1 * half_2
            return memo[n]
        return pow(x, n) if n > 0 else 1 / pow(x, -n)
        
        