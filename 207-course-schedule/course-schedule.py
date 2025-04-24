class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        for a,b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1
        
        path = deque([i for i in range(numCourses) if inDegree[i] == 0])
        visited = set()
        while path:
            p = path.popleft()
            visited.add(p)
            for neigh in graph[p]:
                inDegree[neigh] -= 1
                if not inDegree[neigh]:
                    path.append(neigh)
        return numCourses == len(visited)
        