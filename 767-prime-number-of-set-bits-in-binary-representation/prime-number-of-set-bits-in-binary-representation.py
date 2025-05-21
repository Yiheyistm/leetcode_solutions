class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_nums = { 2, 3, 5, 7, 11, 13, 17, 19} # log10^6 == 24 bits which mean no need to add prime num above 24
        cnt = 0
        for l in range(left, right + 1):
            if l.bit_count() in prime_nums:
                cnt += 1
        return cnt
        