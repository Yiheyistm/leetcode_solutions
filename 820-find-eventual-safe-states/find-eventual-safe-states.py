class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def topSort(node):
            if color[node] == 1:
                return False
            color[node] = 1
            for neigh in graph[node]:
                if color[neigh] == 2:
                    continue
                if not topSort(neigh):
                    return False
            color[node] = 2
            return True

            
        color = [0] * len(graph)
        order = []
        for node in range(len(graph)):
            if color[node] == 1:
                continue
            if color[node] == 2 or topSort(node):
                order.append(node)
        return order