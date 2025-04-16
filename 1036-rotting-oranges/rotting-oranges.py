class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        n, m = len(grid), len(grid[0])

        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        rotten_org = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten_org.append((i, j))
                    visited.add((i, j))

        cnt = 0
        while rotten_org:
            for _ in range(len(rotten_org)):
                i, j = rotten_org.popleft()
                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc
                    if inbound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] != 0:
                        rotten_org.append((nr, nc))
                        visited.add((nr, nc))
            cnt += 1 if len(rotten_org) else 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        return cnt
        

        

        