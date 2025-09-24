class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        # Bottom Up DP with 1D array
        dp = [0] * n
        dp[0]= 1 
        for i in range(m):
            for j in range(n):
                if j > 0:
                    dp[j] +=dp[j -1]
        return dp[-1]
        