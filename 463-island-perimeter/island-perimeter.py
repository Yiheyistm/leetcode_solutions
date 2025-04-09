class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        perm = 0

        def inbound(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] == 0:
                return 1
            elif grid[row][col] == 1:
                return 0
         
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for x, y in direction:
                        nw_r = x + i
                        nw_c = y + j
                        perm += inbound(nw_r, nw_c)
        return perm


        