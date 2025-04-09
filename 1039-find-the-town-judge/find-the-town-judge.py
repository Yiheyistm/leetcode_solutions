class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_i = defaultdict(set)
        for i, j in trust:
            trust_i[i].add(j)

        ans = -1
        for i in range(1,n + 1):
            if len(trust_i[i]) == 0 and ans != -1:
                return -1
            elif len(trust_i[i]) == 0 and ans == -1:
                ans = i

        for i in range(1, n + 1):
            if ans not in trust_i[i] and ans != i: return -1
        return ans




        
        