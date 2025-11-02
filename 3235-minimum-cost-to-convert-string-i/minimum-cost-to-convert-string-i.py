class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def floyd_warshall(adj):
            n = len(adj)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if adj[i][k] + adj[k][j] < adj[i][j]:
                            adj[i][j] = adj[i][k] + adj[k][j]

        adj = [[inf]*26 for _ in range(26)]
        for i in range(26): adj[i][i] = 0

        base = ord('a')
        for f, s, w in zip(original, changed, cost):
            f_idx = ord(f) - base
            s_idx = ord(s) - base
            adj[f_idx][s_idx] = min(adj[f_idx][s_idx], w)

        floyd_warshall(adj)
        res = 0
        for f, s in zip(source, target):
            f_idx = ord(f) - base
            s_idx = ord(s) - base
            short_path = adj[f_idx][s_idx]
            if short_path == inf:
                return -1
            res += short_path
        return res

        
        