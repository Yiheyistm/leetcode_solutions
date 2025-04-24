class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        for a,b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1
        
        path = deque([i for i in range(numCourses) if inDegree[i] == 0])
        res = []
        while path:
            p = path.popleft()
            res.append(p)
            for neigh in graph[p]:
                inDegree[neigh] -= 1
                if not inDegree[neigh]:
                    path.append(neigh)
            if not path and len(res) != numCourses:
                return []
        return res
        