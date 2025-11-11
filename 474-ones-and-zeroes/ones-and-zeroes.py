class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [[s.count("1"), s.count("0")] for s in strs]
        memo = defaultdict(int)
        def dfs(i, remN, remM):
            if remN < 0 or remM < 0:
                return -inf
            if i == len(strs): return 0
            
            if (i, remN, remM) not in memo:
                one, zero = counter[i]
                leave = dfs(i + 1, remN, remM)
                take = 1 + dfs(i + 1, remN - one, remM - zero)
                memo[(i, remN, remM)] = max(leave, take)
            return memo[(i, remN, remM)]
        return dfs(0, n, m)
            
        