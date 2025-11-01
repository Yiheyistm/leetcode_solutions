class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)

        MOD = 10 ** 9 + 7
        f = endPos - startPos
        if k < f or (k - f) % 2:
            return 0

        rem = k - f
        b = rem // 2
        f += b
        return (factorial(k) // (factorial(f) * factorial(b))) % MOD

        