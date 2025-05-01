class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            while x != parent[x]:
                x = parent[parent[x]]
            return x
        def union(x,y):
            parX = find(x)
            parY = find(y)
            if parX != parY:
                if rank[parX] > rank[parY]:
                    parent[parY] = parX
                elif rank[parY] > rank[parX]:
                    parent[parX] = parY
                else:
                    parent[parX] = parY
                    rank[parY] += 1

        n = len(edges)
        parent = {i:i for i in range(1, n + 1)}
        rank = [0] * (n + 1)
        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            union(a,b)




        