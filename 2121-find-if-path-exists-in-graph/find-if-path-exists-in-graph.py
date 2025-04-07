class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(vertex):
            if destination == vertex:
                return True

            visited.add(vertex)
            for neigh in graph[vertex]:
                if neigh not in visited:
                    if dfs(neigh):
                        return True
            return False

        return dfs(source)
        
            



        