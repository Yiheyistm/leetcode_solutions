class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stk = []
        t_stk = []
        for ch in s:
            if not s_stk and ch == '#': continue
            elif s_stk and ch == '#':
                s_stk.pop()
            else:
                s_stk.append(ch)
        for ch in t:
            if not t_stk and ch == '#': continue
            elif t_stk and ch == '#':
                t_stk.pop()
            else:
                t_stk.append(ch)
        return s_stk == t_stk
        