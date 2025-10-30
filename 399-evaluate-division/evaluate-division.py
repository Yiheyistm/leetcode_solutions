class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        weight = {}
        def find(p):
            if parent[p] != p:
                orig_parent = parent[p]
                parent[p] = find(orig_parent)
                weight[p] *= weight[orig_parent]
            return parent[p]

        def union(x, y, val):
            if x not in parent:
                parent[x] = x
                weight[x] = 1
            if y not in parent:
                parent[y] = y
                weight[y] = 1

            px, py = find(x), find(y)
            if px == py:
                return
            parent[px] = py
            weight[px] = val * weight[y] / weight[x]

        def is_connected(x, y):
            if x not in parent or y not in parent:
                return -1
            px, py = find(x), find(y)
            if px != py:
                return - 1
            return weight[x] / weight[y]
            

        for eq,val in zip(equations,values):
            union(eq[0], eq[1], val)
            
        res = []
        for x, y in queries:
            res.append(is_connected(x, y))
        return res

        