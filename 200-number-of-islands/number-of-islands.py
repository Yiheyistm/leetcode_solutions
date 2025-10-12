class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            if (i < 0 or i >= R or j < 0 or j >= C) or grid[i][j] == "0" or (i, j) in visited:
                return 0
            visited.add((i, j))
            ild = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            return ild

        ans = 0
        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and grid[i][j] == "1":
                    ans += dfs(i, j)
        return ans




        