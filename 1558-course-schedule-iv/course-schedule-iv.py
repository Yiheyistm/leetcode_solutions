class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        start = deque([i for i in range(numCourses) if indegree[i] == 0])
        preq = [set() for _ in range(numCourses)]
        while start:
            p = start.popleft()
            for neigh in graph[p]:
                preq[neigh] |= preq[p] | {p}
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    start.append(neigh)
        
        ans = []
        for u, v in queries:
            ans.append(True if u in preq[v] else False)
        return ans
        