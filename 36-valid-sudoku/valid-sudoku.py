class Solution:
    def checker(self,board, idx_lst, a, b) ->bool:
        for idx in idx_lst:
            i, j = idx
            if i == a or j == b:
                return False
        tr_i, tr_j = a // 3, b // 3
        for i in range(tr_i * 3, tr_i * 3 + 3):
            for j in range(tr_j * 3, tr_j * 3 + 3):
                if board[i][j] == board[a][b] and a != i and b != j:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sodoku_map = defaultdict(list)
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell in sodoku_map:
                    ckr = self.checker(board,sodoku_map[cell], i, j)
                    if ckr:
                        sodoku_map[cell].append([i,j])
                    else:
                        return False
                elif cell.isalnum():
                    sodoku_map[cell].append([i,j])
                else:
                    continue
        return True