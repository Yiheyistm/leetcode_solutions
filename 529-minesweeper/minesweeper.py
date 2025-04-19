class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        m, n = len(board), len(board[0])
        sr,sc = click
        
        if board[sr][sc] == 'M':
            board[sr][sc] = 'X'
            return board
            
        path = deque([(sr, sc)])
        visited = {(sr, sc)}
        while path:
            i, j = path.popleft()
            mine_cnt = 0
            b_cnt = 0
            for dr, dc in directions:
                nr, nc = i + dr, j + dc                
                if inbound(nr, nc) and board[nr][nc] == 'M':
                    mine_cnt += 1

            if mine_cnt:
                board[i][j] = str(mine_cnt)
            elif b_cnt or not mine_cnt:
                board[i][j] = 'B'
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if inbound(nr, nc) and (nr, nc) not in visited:
                        path.append((nr, nc))
                        visited.add((nr, nc))

        return board
        