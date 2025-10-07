class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(min(a, b), max(a, b) % min(a, b))
            
        ab = (a * b) // gcd(a, b)
        ac = (a * c) // gcd(a, c)
        bc =  (b * c) // gcd(b, c)
        abc = (ab * c) // gcd(ab, c)
        def check(mid):
            m = (mid // a) + (mid // b) + (mid // c) - (mid // (ab)) - (mid // bc)- (mid // (ac)) + (mid // (abc))
            return n <= m
        low = 0
        high = 2*10**9
        while low + 1 < high:
            mid = (low + high) // 2
            if check(mid): high = mid
            else: low = mid
        return high