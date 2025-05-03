class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph) - 1
        print(n)
        def dfs(s, path):
            path.append(s)
            if s == n:
                paths.append(path[:])
                return

            for neigh in graph[s]:
                dfs(neigh, path)
                path.pop()
            return 

        dfs(0, [])
        return paths
        
        