class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for eq,val in zip(equations,values):
            x,y = eq
            graph[x].append((y,val))
            graph[y].append((x, 1 / val))

        res = []
        for x, y in queries:
            if x in graph and y in graph:
                visit = set()
                qq = deque([(x,1)])
                while qq:
                    f, prod = qq.popleft()
                    if y == f:
                        res.append(prod)
                        break
                    visit.add(f)
                    for neigh, val in graph[f]:
                        if neigh not in visit:
                            qq.append((neigh, prod * val))
                else:
                    res.append(-1)                    
            else: res.append(-1)
        return res

        