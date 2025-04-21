class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [[] for _ in range(n)]
        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)
        for i in range(n):
            path = deque(graph[i])
            visited = set()
            while path:
                p = path.popleft()
                if p not in visited:
                    answer[i].append(p)
                    visited.add(p)
                for ch in graph[p]:
                    if ch not in visited:
                        visited.add(ch)
                        path.append(ch)
                        answer[i].append(ch)

            answer[i].sort()
        return answer
        