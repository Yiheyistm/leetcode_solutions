class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dir = [(0, 1), (1, 0)]
        store = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            if i == m -1 and j == n - 1:
                return 1
            if store[i][j] == -1:
                cnt = 0
                for (di, dj) in dir:
                    cnt += dfs(di + i, dj + j)
                store[i][j] = cnt
            return store[i][j]
        return dfs(0, 0)