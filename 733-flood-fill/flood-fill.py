class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != st_color or visited[r][c]:
                return
            image[r][c] = color
            visited[r][c] = True
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        visited = [[False] * len(image[0]) for _ in range(len(image))]
        rows, cols = len(image), len(image[0])
        st_color = image[sr][sc]
        dfs(sr, sc)
        return image
        