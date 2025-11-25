class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        start = 1
        i = 1
        while start % k and i <= k:
            i += 1
            start = start * 10 + 1
        return i


        
        