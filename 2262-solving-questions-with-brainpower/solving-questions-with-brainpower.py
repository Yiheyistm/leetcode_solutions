class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * (N +1)
        for i in range(N-1, -1, -1):
            point, bpr = questions[i]
            idx = i + bpr + 1 if i + bpr + 1  <= N else i
            dp[i] = max(point + dp[idx], dp[i + 1])
        return dp[0]



