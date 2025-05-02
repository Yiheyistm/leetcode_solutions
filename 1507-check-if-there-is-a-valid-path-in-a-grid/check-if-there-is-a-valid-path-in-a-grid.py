class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        if rows == cols == 1:
            return True
        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        directions = {
            1:[(0, 1), (0, -1)],
            2:[(1, 0), (-1, 0)],
            3:[(0, -1), (1, 0)],
            4:[(0, 1), (1, 0)],
            5:[(0, -1), (-1, 0)],
            6:[(0, 1), (-1, 0)],
        }
        valid_neigh = {
            1: {1, 3, 5, 4, 6},
            2: {2, 5, 6, 3, 4},  
            3: {1, 2, 4, 5, 6},  
            4: {1, 3, 2, 5, 6},  
            5: {1, 6, 2, 3, 4},  
            6: {1, 5, 2, 3, 4} 
        }

        backward_path = deque([(rows - 1, cols - 1)])
        visited = set()
        while backward_path:
            r,c = backward_path.popleft()
            p = grid[r][c]
            visited.add((r, c))
            for dr,dc in directions[p]:
                nr, nc = r + dr, c + dc
                if nr == 0 and nc == 0:
                    return True
                if inbound(nr, nc) and (nr, nc) not in visited:
                    nxt = grid[nr][nc]
                    if nxt in valid_neigh[p]:
                        backward_path.append((nr, nc))

        return False

