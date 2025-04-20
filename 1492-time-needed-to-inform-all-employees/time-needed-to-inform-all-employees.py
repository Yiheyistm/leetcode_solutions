class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if i == headID: continue
            graph[manager[i]].append(i)
        path = deque([headID])
        time = 0
        while path:
            p = path.popleft()
            tm = informTime[p]
            time = max(time, tm)
            for ch in graph[p]:
                if informTime[ch]:
                    informTime[ch] += tm
                    path.append(ch)
        return time


