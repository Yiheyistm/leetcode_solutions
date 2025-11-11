class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = defaultdict(int)
        def dfs(i, remN, remM):
            if i == len(strs):
                return 0
            if (i, remN, remM) not in memo:
                binary = strs[i]
                one = binary.count("1")
                zero = binary.count("0")

                leave = dfs(i + 1, remN, remM)
                take = 0
                if remN >= one and remM >= zero:
                    take = 1 + dfs(i + 1, remN - one, remM - zero)
                memo[(i, remN, remM)] = max(leave, take)
            return memo[(i, remN, remM)]
        return dfs(0, n, m)
            
        