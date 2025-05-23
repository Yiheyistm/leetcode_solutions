class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (len(coins))
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        # remove leaf node with no coins
        leafWithoutCoins = deque([i for i in range(len(coins)) if indegree[i]== 1 and coins[i] == 0])
        while leafWithoutCoins:
            p = leafWithoutCoins.popleft()
            for neigh in graph[p]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1 and coins[neigh]== 0:
                    leafWithoutCoins.append(neigh)
            del graph[p]
            

        # remove leaf node with coins and their parents
        leafWithCoins = [i for i in range(len(coins)) if indegree[i] == 1 and coins[i] == 1]
        while leafWithCoins:
            p = leafWithCoins.pop()
            for neigh in graph[p]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1:
                    del graph[neigh]
            del graph[p]
        
        return (len(graph) - 1) * 2 if len(graph) > 1 else 0

        