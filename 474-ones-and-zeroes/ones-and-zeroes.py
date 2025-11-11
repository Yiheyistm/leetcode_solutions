class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [[s.count("1"), s.count("0")] for s in strs]
        @cache
        def dfs(i, remN, remM):
            if remN < 0 or remM < 0:
                return -inf
            if i == len(strs): 
                return 0

            one, zero = counter[i]
            # take and leave
            return max(dfs(i + 1, remN, remM), 1 + dfs(i + 1, remN - one, remM - zero))
        return dfs(0, n, m)
            
        