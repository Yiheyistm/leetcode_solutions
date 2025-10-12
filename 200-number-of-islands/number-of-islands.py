class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    ans += 1
                    path = deque([(i, j)])
                    while path:
                        r, c = path.popleft()
                        for di, dj in [(r + 1, c), (r - 1, c),(r, c - 1),(r, c + 1)]:
                            if (di < 0 or di >= R or dj < 0 or dj >= C) or grid[di][dj] == "0":
                                continue
                            path.append((di, dj))
                            grid[di][dj] = "0"
        return ans




        