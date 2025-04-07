class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        Coloring
        -1 = Red
        -2 = Blue
        '''
        bipart = defaultdict(int)
        
        for i in range(len(graph)):
            if bipart[i] == 0:
                bipart[i] = -1
                dq = deque([i])
                while dq:
                    pp = dq.popleft()
                    nx_cr = -1 if bipart[pp] == -2 else -2
                    for neigh in graph[pp]:
                        if bipart[neigh] == 0:
                            bipart[neigh] = nx_cr
                            dq.append(neigh)
                        elif bipart[neigh] == bipart[pp]:
                            return False

        return True


        