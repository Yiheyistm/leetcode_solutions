class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:



        graph = defaultdict(list)
        min_scores = [float('inf') for _ in range(n + 1)]
        for a, b, d  in roads:
            min_scores[a] = min(d,min_scores[a])
            min_scores[b] = min(d,min_scores[b])
            graph[a].append(b)
            graph[b].append(a)

        min_score = float('inf')
        visit = set()
        path = [1]
        while path:
            p = path.pop()
            min_score = min(min_score, min_scores[p])
            visit.add(p)
            for neigh in graph[p]:
                if neigh not in visit:
                    path.append(neigh)
        

        return min_score
        