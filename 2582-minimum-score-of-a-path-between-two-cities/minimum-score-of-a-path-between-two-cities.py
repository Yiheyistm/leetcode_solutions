class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]

        def union(x, y, dis):
            parX = find(x)
            parY = find(y)
            if parX != parY:
                if size[parX] >= size[parY]:
                    parent[parY] = parX
                    size[parX] += size[parY]
                    min_score[parX] = min(min_score[parX], min_score[parY], dis)
                else:
                    parent[parX] = parY
                    size[parY] += size[parX]
                    min_score[parY] = min(min_score[parX], min_score[parY], dis)
            else:
                min_score[parY] = min(dis, min_score[parY])


        parent = [i for i in range(n + 1)]
        size = [1 for _ in range(n + 1)]
        min_score = [float('inf') for _ in range(n + 1)]
        for a, b, d  in roads:
            min_score[a] = min(d,min_score[a])
            min_score[b] = min(d,min_score[b])
            union(a, b, d)

        return min_score[find(1)]
        