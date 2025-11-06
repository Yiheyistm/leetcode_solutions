class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            par1 = find(u)
            par2 = find(v)
            if par1 != par2:
                if size[par1] < size[par2]:
                    par1, par2 = par2, par1
                
                parent[par2] = par1
                size[par1] += size[par2]
                while stations[par2]:
                    heappush(stations[par1], heappop(stations[par2]))
                


        parent = {i:i for i in range(1, c + 1)}
        size = [1] * (c + 1)

        non_functional = set()
        stations = defaultdict(list)
        for i in range(1, c + 1):
            heappush(stations[i], i)

        for u,v in connections: # n
            union(u, v) # log(n)

        res = []

        for op, st in queries: # n
            if op == 1:
                if st not in non_functional:
                    res.append(st)
                else:
                    par = find(st) # log(n)
                    while stations[par] and stations[par][0] in non_functional: # log(n)
                        heappop(stations[par])

                    if stations[par]:
                        res.append(stations[par][0])
                    else:
                        res.append(-1)
            else:
                non_functional.add(st)
        return res
        # O(nlog(n))