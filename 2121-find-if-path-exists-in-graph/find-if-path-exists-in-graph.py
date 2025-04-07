class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set([source])
        stack = [source]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        while stack:
            node = stack.pop()
            if destination == node:
                return True

            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)

        return False

            



        