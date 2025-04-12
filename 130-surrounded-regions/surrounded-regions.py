class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
                        # LEFT   TOP     RIGHT   BOTTOM
        directions = [(0, -1), (-1, 0),(0, 1), (1,0)]
        def dfs(r, c):
            if (r < 0 or r >= n or c < 0 or c >= m) or board[r][c] == 'X' or board[r][c] == 'C':
                return 
            board[r][c] = 'C'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
 
        n = len(board)
        m = len(board[0])
        # traverse around the boarder of the region
        for i in range(n): # traverse around row boarder
            dfs(i,0)
            dfs(i, m - 1)
        for j in range(m): # Traverse around cols boarder
            dfs(0, j)
            dfs(n - 1, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'C':
                    board[i][j] = 'O'
                


             