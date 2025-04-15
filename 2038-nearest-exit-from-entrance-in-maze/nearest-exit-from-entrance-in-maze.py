class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inbound(r, c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0])

        directions = [(0,-1), (0, 1), (1, 0), (-1, 0)]
        path = deque()
        sr, sc = entrance
        visited = {(sr,sc)}
        for dr, dc in directions:
                nr = sr + dr
                nc = sc + dc
                if inbound(nr, nc) and maze[nr][nc] == '.':
                    path.append((nr, nc))
                    visited.add((nr, nc))
        step  = 1
        while path:
            for _ in range(len(path)):
                i, j = path.popleft()
                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc
                    if not inbound(nr, nc):
                        return step
                    if inbound(nr, nc) and (nr, nc) not in visited and maze[nr][nc] == '.':
                        visited.add((nr, nc))
                        path.append((nr, nc))
            step += 1
        return -1
                



        