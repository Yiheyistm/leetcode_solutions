class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def dfs(n):
            if n == 1:
                return 0
            if n not in memo:
                memo[n] = 1 + dfs((3 * n) + 1 if n & 1 else n // 2)
            return memo[n]

        ans = list(range(lo, hi+1))
        ans.sort(key=lambda x: dfs(x))
        return ans[k-1]
        