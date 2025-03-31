class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return
            for b in ['0', '1']:
                if s and s[-1] == b == '0':continue
                nw = s + b
                backtrack(nw)
        backtrack('')
        return res

        