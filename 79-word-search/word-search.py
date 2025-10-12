class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        root = {}
        node = root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["end"] = 1


        visited = set()
        def dfs(i, j, node):
                if not (0 <= i < R) or not (0 <= j < C) or board[i][j] not in node or (i, j) in visited:
                    return False
                    
                ch = board[i][j]
                node = node[ch]
                if "end" in node:
                    return True
                    
                ans = False
                visited.add((i, j))
                ans |= dfs(i + 1, j, node)
                ans |= dfs(i - 1, j, node)
                ans |= dfs(i, j - 1, node)
                ans |= dfs(i, j + 1, node)
                visited.remove((i, j))
                return ans

        for i in range(R):
            for j in range(C):
                if dfs(i, j, root):
                    return True
        return False

        