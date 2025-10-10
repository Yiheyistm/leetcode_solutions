class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n = len(board), len(board[0])
        def inBound(i, j):
            return 0 <= i < m and 0 <= j < n

        root = {}
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr["/"] = 1
        
        
        res = set()
        visit = set()
        def dfs(i,j, node, word):
            if not inBound(i, j) or (i, j) in visit or board[i][j] not in node:
                return
            
            visit.add((i, j))
            ch = board[i][j]
            node = node[ch]
            word += ch
            if '/' in node:
                res.add(word)
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            visit.remove((i, j))
                
        for i in range(m):
            for j in range(n):
                dfs(i,j, root,'')
                
        return list(res)

        