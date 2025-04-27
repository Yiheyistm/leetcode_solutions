class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def findRowCol(cell):
            cell -= 1
            r = (n - 1) - (cell // n)
            if (n - 1 - r) % 2 == 0:
                c = cell % n
            else:
                c = (n - 1) - (cell % n)
            return r, c


        n = len(board)
        start = deque([1])
        min_move = 0
        visited = set([1])
        while start:
            for _ in range(len(start)):
                curr = start.popleft()
                if curr == n ** 2:
                    return min_move
                for nxt in range(curr + 1, min(curr + 6, n ** 2) + 1):
                    r, c = findRowCol(nxt)
                    dest = board[r][c] if board[r][c] != -1 else nxt
                    if dest not in visited:
                        visited.add(dest)
                        start.append(dest)
            min_move += 1

        
        return -1



        