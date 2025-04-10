class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not len(edges) and n == 1:
            return 0
        in_degree = defaultdict(int)
        visited = set()
        for s,w in edges:
            visited.add(s)
            visited.add(w)
            in_degree[w] += 1

        champ = [node for node in visited if in_degree[node] == 0]
        return champ[0] if len(visited) == n and len(champ) == 1 else -1
  
                



            
        