class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        city = [None, inf]
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        for i in range(n):
            visit = set()
            min_heap = [(0, i)] # (weight, node)
            while min_heap:
                w1, node = heappop(min_heap)
                if node in visit:
                    continue
                visit.add(node)
                for neigh, w in graph[node]:
                    if w1 + w <= distanceThreshold:
                        heappush(min_heap, (w1 + w, neigh))

            no_visited_city = len(visit)
            if city[0] == None or city[1] >= no_visited_city:
                city = [i, no_visited_city]
        return city[0]

        