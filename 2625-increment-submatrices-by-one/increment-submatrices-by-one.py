class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*(n + 1) for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for i in range(r1, r2 + 1):
                mat[i][c1] += 1
                mat[i][c2 + 1] -= 1
        res = []
        for row in mat:
            pfx = list(accumulate(row[:-1]))
            res.append(pfx)
        return res

            