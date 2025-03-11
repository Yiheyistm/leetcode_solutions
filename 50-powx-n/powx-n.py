class Solution:
    def myPow(self, x: float, n: int) -> float:
       
        @cache 
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            y1 = pow(x, n//2)
            y2 = pow(x, n-(n // 2))
            return y1 * y2 
            
        if n > 0:
            return pow(x, n)
        return 1 / (pow(x,-n))

        