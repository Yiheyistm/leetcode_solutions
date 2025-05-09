class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parX = find(x)
            parY = find(y)
            if parX != parY:
                parent[parY]= parX
                return True
            return False

        parent = {i:i for i in range(len(points))}
        parent_weight = []
        for i in range(len(points)):
            min_ = (float('inf'), 0) # (weight, j)
            x1, y1 = points[i]
            for j in range(len(points)):
                if i != j:
                    x2, y2 = points[j]
                    manhattan_dis = abs(x1 - x2) + abs(y1 - y2)
                    parent_weight.append((manhattan_dis, (i, j)))
            
        parent_weight.sort()
        tot_weight = 0
        for w, (u, v) in parent_weight:
            if union(u, v):
                tot_weight += w
                    
        return tot_weight
        

        