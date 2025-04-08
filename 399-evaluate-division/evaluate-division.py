class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(s,d):
            if s == d:
                return 1

            visit.add(s)
            for neigh,val in graph[s]:
                if neigh not in visit:
                    prod = dfs(neigh, d)
                    if prod != -1:
                        prod *= val
                        return prod
            return -1

        graph = defaultdict(list)
        for eq,val in zip(equations,values):
            x,y = eq
            graph[x].append((y,val))
            graph[y].append((x, 1 / val))

        res = []
        for x, y in queries:
            if x in graph and y in graph:
                visit = set()
                res.append(dfs(x, y))
            else: res.append(-1)
        return res

        