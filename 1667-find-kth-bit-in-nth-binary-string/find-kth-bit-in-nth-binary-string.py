class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recur(s, n):
            if n == 1:
                return s
            x = '1' + ''.join('0' if bn == '1' else '1' for bn in s)[::-1]
            nwS = s + x
            return recur(nwS, n-1)
        val =  recur('0', n)
        return val[k-1]