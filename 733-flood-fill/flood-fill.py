class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        dq = deque([(sr, sc)])
        visited = [[False] * len(image[0]) for _ in range(len(image))]
        st_color = image[sr][sc]
        image[sr][sc] = color
        while dq:
            x, y = dq.popleft()
            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == st_color and not visited[nr][nc]:
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    image[nr][nc] = color
        return image
        