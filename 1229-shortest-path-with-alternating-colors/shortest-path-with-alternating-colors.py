class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        for a, b in redEdges:
            red_graph[a].append(b)

        blue_graph = defaultdict(list)
        for a, b in blueEdges:
            blue_graph[a].append(b)

        visited = set()
        dq = deque([(0, 0, 'R'), (0, 0, 'B')])
        result = [-1] * n

        while dq:
            node, steps, color = dq.popleft()
            if (node, color) in visited:
                continue
            
            if result[node] == -1:
                result[node] = steps
            result[node] = min(result[node], steps)
            visited.add((node, color))
            if color == 'R':
                nxt_color = 'B'
                nxt_node = blue_graph[node]
            if color == 'B':
                nxt_color = 'R'
                nxt_node = red_graph[node]

            for neigh in nxt_node:
                dq.append((neigh, steps + 1, nxt_color))
        return result