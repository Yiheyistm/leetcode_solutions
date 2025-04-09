class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        perm = 0

        def inbound(r, c):
            return (0 <= r < rows and 0 <= c < cols)
      
        def dfs(row, col):
            nonlocal perm
            grid[row][col] = -1
            for x, y in direction:
                nw_r = x + row
                nw_c = y + col
                if inbound(nw_r, nw_c) and grid[nw_r][nw_c] == 1:
                    dfs(nw_r, nw_c)
                elif not inbound(nw_r, nw_c) or grid[nw_r][nw_c] == 0:
                    perm += 1

        isFound = False  
        for i in range(rows):
            if isFound: break
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    isFound = True
                    break
        return perm


        