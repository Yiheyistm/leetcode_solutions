class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Five Evens digits which is 0 2 4 6 8
        # Four Prime digits 2 3 5 7
        MOD = 10**9 + 7
        return (pow(5, n - n//2, MOD) * pow(4 , n//2, MOD)) % MOD
        # ((5 ** (n - n//2)%MOD) * (4 ** (n//2)) % MOD) % MOD