class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s)
        return '1'*(cnt['1'] -1) + '0' * cnt['0'] + '1'
        