class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def inbound(r, c):
            return 0 <= r < len(isWater) and 0 <= c < len(isWater[0])

        directions = [(0,-1), (0, 1), (1, 0), (-1, 0)]
        path = deque()
        visited = set()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    path.append((i, j))
                    visited.add((i, j))
                    isWater[i][j] = 0

        step = 1
        
        while path:
            for _ in range(len(path)):
                i, j = path.popleft()
                for dr, dc in directions:
                    nr = i + dr
                    nc = j + dc
                    if inbound(nr, nc) and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        path.append((nr, nc))
                        isWater[nr][nc] = step

            step += 1
        
        return isWater
        