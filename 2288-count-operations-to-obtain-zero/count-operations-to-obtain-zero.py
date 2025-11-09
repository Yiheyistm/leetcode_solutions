class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        
        cnt = 0
        while True:
            num1, num2 = max(num1, num2), min(num1, num2)
            cnt += 1
            num1 -= num2
            if num1 == 0:
                return cnt
                
        
        