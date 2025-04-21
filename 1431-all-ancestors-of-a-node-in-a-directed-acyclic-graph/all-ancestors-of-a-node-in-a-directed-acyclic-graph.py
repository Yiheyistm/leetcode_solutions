class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for _ in range(n)]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if not indegree[i]:
                q.append(i) 
        
        while q:
            p = q.popleft()
            for neigh in graph[p]:
                answer[neigh] |= answer[p] | {p}
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    q.append(neigh)
            answer[p] = sorted(answer[p])
        return answer
        