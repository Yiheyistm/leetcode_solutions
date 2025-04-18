class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0,-1), (0, 1), (1, 0), (-1, 0)]
        path = deque()
        visited = [[False] * cols for _ in range(rows)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    path.append((i, j, 1))
                    visited[i][j] = True
    
        while path:
            i, j, length = path.popleft()
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc
                if (0 <= nr < rows and 0 <= nc < cols) and not visited[nr][nc]:
                    visited[nr][nc] = True
                    path.append((nr, nc, length +  1))
                    mat[nr][nc] = length    
        return mat
        