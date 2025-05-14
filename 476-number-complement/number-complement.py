class Solution:
    def findComplement(self, num: int) -> int:
        n = floor(log(num, 2)) + 1
        return num ^ ((1 << n ) - 1)

        