class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 3: return 2

        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            temp = a + b + c
            a = b
            b = c
            c = temp
        return c

        