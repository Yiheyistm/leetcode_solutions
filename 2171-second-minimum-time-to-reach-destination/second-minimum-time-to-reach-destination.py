class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        second_min = None
        visited = set()
        heap = [(0, 1)]
        dist = defaultdict(list)
        while heap:
            t, node = heappop(heap)
            if dist[node] and dist[node][0] == t or len(dist[node]) == 2:
                continue

            dist[node].append(t)
            if node == n and len(dist[node]) == 2:
                return t

            if (t // change) % 2 == 1:
                t = (t // change + 1) * change # the next green light
            for neigh in adj[node]:
                if len(dist[neigh]) < 2:
                    heappush(heap, (t + time, neigh))
        