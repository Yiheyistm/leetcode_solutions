class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        pfx = [1] * n
        for i in range(k):
            for j in range(1, n):
                pfx[j] += pfx[j -1]
        return pfx[-1] % (10**9 + 7)

        