class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        
        cnt = 0
        while True:
            mx, mn =max(num1, num2), min(num1, num2)
            q, r = divmod(mx, mn)
            cnt += q
            if not r:
                return cnt
            num1 = mn
            num2 = r
                
        
        