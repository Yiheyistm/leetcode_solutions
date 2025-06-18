class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
            if indegree[a] > 1:
                return a
            if indegree[b] > 1:
                return b
        