class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        lst = list(range(1, n+1))
        print(lst)
        while len(lst) > 1:
            n = i + k - 1
            l = n % (len(lst))
            m =lst.pop(l)
            i = l
            
            print(m,n, i, lst)
        return lst[0]

        