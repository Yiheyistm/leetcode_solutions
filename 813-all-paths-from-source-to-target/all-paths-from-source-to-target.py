class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        stack = [[0]]
        
        while stack:
            current_path = stack.pop()
            node = current_path[-1]
            
            if node == target:
                res.append(current_path)
                continue 

            for neigh in graph[node]:
                new_path = list(current_path)
                new_path.append(neigh)
                stack.append(new_path)
                                
        return res

        # target = len(graph) - 1
        # res = []
        # def dfs(node, store):
        #     if node == target:
        #         res.append(store[:])
        #         return

        #     for neigh in graph[node]:
        #         store.append(neigh)
        #         dfs(neigh, store)
        #         store.pop()
        #     return

        # dfs(0, [0])
        # return res

        