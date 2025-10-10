class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        cnt = 1
        for s1, t1 in zip(s, t):
            if s_dict[s1] != t_dict[t1]:
                return False
            s_dict[s1] = cnt
            t_dict[t1] = cnt
            cnt += 1

        return True
        