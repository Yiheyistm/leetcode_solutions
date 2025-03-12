class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [] # (value , count)
        for ch in s:
            if stk and stk[-1][0] == ch:
                stk[-1][1] += 1
            else:
                stk.append([ch, 1])
            if stk[-1][1] == k:
                stk.pop()

        res = ''
        for ch, n in stk:
            res += (ch * n) # because every character found n times in stk
        return res
        