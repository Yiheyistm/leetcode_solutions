class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(s, edge):
            visited.add(s)
            flag = True
            cnt = 1
            for neigh in graph[s]:
                if neigh not in visited:
                    isvalid, count = dfs(neigh, edge)
                    cnt += count
                    if isvalid:
                        continue
                    else:
                        flag =  False

  
            return len(graph[s]) == edge and flag, cnt
            

        graph = defaultdict(list)
        visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        cnt  = 0
        for i in range(n):
            if i not in visited:
                isConnected, no_edges = dfs(i,len(graph[i]))
                if isConnected and no_edges - 1 == len(graph[i]):
                    cnt += 1
        return cnt
        