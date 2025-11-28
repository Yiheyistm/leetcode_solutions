#KN
class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        self.count = 0
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            total = values[node]  
            for nei in g[node]:
                if not visited[nei]:
                    total += dfs(nei)
            if total % k == 0:
                self.count += 1
                return 0   
            return total
        dfs(0)
        return self.count