class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def topSort(node):
            if color[node] == 1:
                return False
            color[node] = 1
            for ch in graph[node]:
                if color[ch] == 2: continue
                if not topSort(ch):
                    return False
            order.append(node)
            color[node] = 2
            return True

        graph = defaultdict(list)
        color = [0 for _ in range(numCourses)] # 0 -> White, 1 -> Grey, 2 -> Black
        order = []
        for a,b in prerequisites:
            graph[b].append(a)
        
        for node in range(numCourses):
            if color[node] != 0: continue
            if not topSort(node):
                return []

        return order[::-1]