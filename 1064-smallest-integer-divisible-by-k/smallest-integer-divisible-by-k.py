class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        st = set()
        start = 0
        i = 0
        while len(st) <= k:
            i += 1
            start = start * 10 + 1
            rem = start % k
            if not rem:
                return i
            st.add(rem)
        return -1


        
        