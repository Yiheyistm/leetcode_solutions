'''
if a number is power of two its binary num has exactly one 1 (100) for 4 
and the number -1 has flip nums 4 -1 = 3 (011)
so 3 AND 4 --> 100 AND 011 = 0
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0