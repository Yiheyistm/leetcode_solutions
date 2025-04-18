class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0),(-1, -1), (-1, 1),(1, -1), (1, 1) ]
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        path = deque([(0, 0, 1)])
        while path:
            i, j, p = path.popleft()
            for dr, dc in directions:
                nr = i + dr; nc = j + dc
                if  i == n - 1 and j == n -1:
                    return p
                elif 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and not visited[nr][nc]:
                    path.append((nr, nc, p +  1))
                    visited[nr][nc] = True

        return -1

        