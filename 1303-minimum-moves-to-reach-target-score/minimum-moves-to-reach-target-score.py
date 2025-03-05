class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c = 0
        nw_trg = target
        while maxDoubles and nw_trg > 1:
            q, r = divmod(nw_trg, 2)
            nw_trg = q
            c += 1 + r
            maxDoubles -= 1 
        return c + nw_trg - 1
        