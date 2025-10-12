class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(i, j, idx):
                if idx == len(word):
                    return True

                if not (0 <= i < R) or not (0 <= j < C) or board[i][j] != word[idx]:
                    return False
                ans = False
                temp = board[i][j]
                board[i][j] = '#'
                ans |= dfs(i + 1, j, idx + 1)
                ans |= dfs(i - 1, j, idx + 1)
                ans |= dfs(i, j - 1, idx + 1)
                ans |= dfs(i, j + 1, idx + 1)
                board[i][j] = temp
                return ans

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True
        return False

        