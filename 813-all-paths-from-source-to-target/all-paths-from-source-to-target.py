class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        def dfs(node, store):
            if node == target:
                res.append(store[:])
                return

            for neigh in graph[node]:
                store.append(neigh)
                dfs(neigh, store)
                store.pop()
            return

        dfs(0, [0])
        return res

        