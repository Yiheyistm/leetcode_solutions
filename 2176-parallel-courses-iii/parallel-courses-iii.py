class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        month_ = [0] * (n + 1) # the maximum month from its previous courses
        
        for prev, nxt in relations:
            graph[prev].append(nxt)
            indegree[nxt] += 1

        path = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                path.append(i)
                month_[i] = time[i - 1]

        while path:
                p = path.popleft()
                for neigh in graph[p]:
                    month_[neigh] = max(month_[neigh], month_[p] + time[neigh - 1])
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        path.append(neigh)

        return max(month_)
       
        