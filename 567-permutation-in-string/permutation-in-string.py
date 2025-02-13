class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m =len(s2), len(s1)
        s1_cntr = Counter(s1)
        s2_cntr = Counter(s2[:m])

        for i in range(m, n):
            if s2_cntr == s1_cntr:
                return True
            s2_cntr[s2[i]] = s2_cntr.get(s2[i], 0) + 1
            s2_cntr[s2[i - m]] -= 1 
            if s2_cntr[s2[i - m]] == 0:
                del s2_cntr[s2[i - m]]
            
        return s2_cntr == s1_cntr
        