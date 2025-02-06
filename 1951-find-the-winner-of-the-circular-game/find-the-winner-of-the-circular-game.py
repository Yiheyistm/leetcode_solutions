class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        lst = list(range(1, n+1))
        while len(lst) > 1:
            n = i + k - 1
            l = n % (len(lst))
            m =lst.pop(l)
            i = l
            
        return lst[0]

        