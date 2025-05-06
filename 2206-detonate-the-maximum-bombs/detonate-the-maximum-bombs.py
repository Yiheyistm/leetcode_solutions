class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(node, visited):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh, visited)
                    
            return len(visited)
            
        graph = defaultdict(list)
        for i, [x1, y1, r1] in enumerate(bombs):
            for j, [x2, y2, r2] in enumerate(bombs):
                if i != j:
                    distance = (x2 - x1)**2 + (y2 - y1)**2
                    if distance <= r1**2:
                        graph[i].append(j)

        no_bombs = 1
        for i in range(len(bombs)):            
            no_bombs = max(dfs(i, set()), no_bombs)
        return no_bombs

        