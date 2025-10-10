class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = defaultdict(int)
        for num in range(lo, hi + 1):
            n = num
            path = []
            while n not in memo and n != 1:
                path.append(n)
                n =  3 * n + 1 if n % 2 else n // 2
                
            steps = memo[n]
            for node in reversed(path):
                steps += 1
                memo[node] = steps

        arr = [(num, memo[num]) for num in range(lo, hi + 1)]
        arr.sort(key=lambda x: (x[1], x[0]))
        return arr[k - 1][0]


        # def dfs(n):
        #     if n == 1:
        #         return 0
        #     if n not in memo:
        #         memo[n] = 1 + dfs((3 * n) + 1 if n & 1 else n // 2)
        #     return memo[n]

        # ans = list(range(lo, hi+1))
        # ans.sort(key=lambda x: dfs(x))
        # return ans[k-1]
        