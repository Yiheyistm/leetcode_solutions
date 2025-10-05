class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        memo = [-1] * N
        def dfs(i):
            if i >= N:
                return 0
            if memo[-1] == -1:
                leave = dfs(i + 1)
                take = questions[i][0] + dfs(i + questions[i][1] + 1)
                memo[i] = max(leave, take)
            return memo[i]
        return dfs(0)
        



