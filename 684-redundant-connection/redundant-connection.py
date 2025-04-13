class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(ch, p, visited):
            visited.add(ch)
            for neigh in graph[ch]:
                if neigh not in visited:
                    if dfs(neigh,ch, visited):
                        return True
                elif neigh != p:
                    return True
            return False

        graph = defaultdict(list)
        for a, b in edges:
            visited = set()
            graph[a].append(b)
            graph[b].append(a)
            if dfs(a, None, visited):
                return [a, b]




        