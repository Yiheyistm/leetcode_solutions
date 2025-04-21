class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(p):
            temp = True
            for neigh in hates[p]:
                if color[neigh] == -1:
                    if color[p] == 0:
                        color[neigh] = 1
                    else:
                        color[neigh] = 0
                    temp = temp and dfs(neigh)
                elif color[p] == color[neigh]:
                    return False
            return temp

        hates = defaultdict(list)
        for a, b in dislikes:
            hates[a].append(b)
            hates[b].append(a)

        color = [ -1 for _ in range(n + 1)]
        ans = True
        for node in range(1, n + 1):
            if color[node] == -1:
                color[node] = 0
                ans = ans and dfs(node)
        return ans

        