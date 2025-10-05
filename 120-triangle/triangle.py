class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        memo = {}
        def dfs(i, j):
            if i >= N:
                return 0
            if j >= len(triangle[i]):
                return 0
            if (i, j) not in memo:
                memo[(i, j)] = triangle[i][j] + min(dfs(i+1, j), dfs(i+1, j + 1))
            return memo[(i, j)]
        return dfs(0, 0)
        