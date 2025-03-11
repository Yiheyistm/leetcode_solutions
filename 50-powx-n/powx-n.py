class Solution:
    def myPow(self, x: float, n: int) -> float:
       
        memo = defaultdict(int)
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            y1 = memo.get(n//2) if n // 2 in memo else pow(x, n//2)
            y2 = memo.get(n-(n // 2)) if n-(n // 2) in memo else pow(x, n-(n // 2))

            memo[n // 2] = y1
            memo[n-(n // 2)] = y2
            return y1 * y2 
            
        return pow(x, n) if n > 0 else 1 / (pow(x,-n))

        