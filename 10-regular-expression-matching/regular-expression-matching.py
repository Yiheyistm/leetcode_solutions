class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        store = [[-1] * N for _ in range(M)]

        def dfs(l, r):
            if l >= M or r >= N:
                for i in range(r, N):
                    if p[i] != '*':
                        if i + 1 >= N or p[i + 1] != '*':
                            return False
                
                return l == M
            
            if store[l][r] == -1:
                if r + 1 < N and p[r + 1] == '*':
                    i = l

                    while i < M and (p[r] == '.' or s[i] == p[r]):
                        if dfs(i, r + 2):
                            store[l][r] = True
                            break
                        i += 1

                    if store[l][r] == -1:
                        store[l][r] = dfs(i, r + 2)
                else:
                    store[l][r] = (p[r] == '.' or s[l] == p[r]) and dfs(l + 1, r + 1)
            
            return store[l][r]
        
        return dfs(0, 0)