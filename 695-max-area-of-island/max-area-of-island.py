class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid); cols = len(grid[0])
        max_area = 0
        def dfs(row, col):
            nonlocal max_area
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0:
                return 0
            cnt = 0
            grid[row][col] = 0
            cnt += dfs(row - 1, col)
            cnt += dfs(row + 1, col)
            cnt += dfs(row, col - 1)
            cnt += dfs(row, col + 1)
            cnt += 1
            max_area = max(max_area, cnt)
            return cnt

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
        return max_area

        