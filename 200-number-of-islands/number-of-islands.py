class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, -1), (-1, 0),(0, 1), (1,0)]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            for i, j in directions:
                nw_row = row + i
                nw_col = col + j
                dfs(nw_row, nw_col)
        
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt

        