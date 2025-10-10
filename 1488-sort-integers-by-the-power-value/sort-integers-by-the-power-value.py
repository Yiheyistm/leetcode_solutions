class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def dfs(n):
            if n == 1:
                return 0
            if n not in memo:
                memo[n] = 1 + dfs((3 * n) + 1 if n % 2 else n // 2)
            return memo[n]
            
        ans = []
        for n in range(lo, hi + 1):
            ans.append((dfs(n), n))
        ans.sort()
        return ans[k-1][1]
        