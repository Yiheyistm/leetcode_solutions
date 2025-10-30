class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mn = inf
        graph = defaultdict(list)
        for u,v,time in times:
            graph[u].append((v, time))

        qq = [(0, k)]
        visited = set()
        while qq:
            time, node = heappop(qq)
            visited.add(node)
            if len(visited) == n:
                return time

            for neigh, t in graph[node]:
                if neigh not in visited:
                    heappush(qq, (time + t, neigh))



        return -1