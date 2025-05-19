class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, k) % (10**9 + 7) # Combination with repeatition

        