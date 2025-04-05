class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def can_place(k, i, store):
            for j in range(k):
                if store[j] == i or abs(store[j] - i) == abs(j - k):
                    return False
            return True
        
        def Nqueens(k, store, ans):
            if k == n:
                nonlocal res
                temp = []
                for row in ans:
                    temp.append(''.join(row))
                res.append(temp)
                return
            for i in range(n):
                if can_place(k, i, store):
                    store[k] = i
                    ans[k][i]= 'Q'
                    Nqueens(k + 1, store, ans)
                    ans[k][i] = '.'
                    store[k] = -1

        store = [-1] * n
        ans = [['.'] * n for _ in range(n)]
        Nqueens(0, store, ans)
        return res
