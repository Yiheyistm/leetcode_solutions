class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i,(a, b) in enumerate(edges):
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))

        max_heap = [(-1, start_node)]
        visit = set()
        while max_heap:
            prob, node = heappop(max_heap)
            visit.add(node)
            if end_node in visit:
                return -prob
            for neigh, p in adj[node]:
                if neigh not in visit:
                    heappush(max_heap, (prob * p, neigh))
        return 0


        