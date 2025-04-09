class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(s):
            for j, val in enumerate(isConnected[s]):
                isConnected[s][j] = 0
                if val == 1 and j != s:
                    dfs(j)

        cnt = 0
        for i in range(len(isConnected)):
            if isConnected[i][i] == 1:
                dfs(i)
                cnt += 1
        return cnt
            
            

        