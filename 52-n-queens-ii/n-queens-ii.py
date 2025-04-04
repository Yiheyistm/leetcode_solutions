class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(k, i,store):
            for j in range(k):
                if store[j] == i or abs(store[j] - i) == abs(j - k):
                    return False
            return True

        def Nqueens(k, store):
            nonlocal cnt
            if k == n:
                cnt += 1
                return
            for i in range(n):
                if can_place(k, i, store):
                    store[k] = i
                    Nqueens(k + 1, store)
                    store[k] = -1
        cnt = 0
        store = [-1] * n
        Nqueens(0, store)
        return cnt
            
        