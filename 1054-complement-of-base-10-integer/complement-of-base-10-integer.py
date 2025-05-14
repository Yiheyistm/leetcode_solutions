class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        x = floor(log(n, 2)) + 1
        return n ^ ((1 << x ) - 1)

        
        