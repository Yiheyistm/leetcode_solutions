class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(p):
            temp = True
            for neigh in graph[p]:
                if color[neigh] == -1:
                    if color[p] == 0:
                        color[neigh] = 1
                    else:
                        color[neigh] = 0
                    temp = temp and dfs(neigh)
                elif color[p] == color[neigh]:
                    return False
            return temp


        color = [ -1 for _ in range(len(graph))]
        ans = True
        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                ans = ans and dfs(node)
        return ans

        


        