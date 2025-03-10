class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0] # 0 is help to track at each depth and it helps to be sure the stk not empty after pop
        for ch in s:
            if ch == '(':
                stk.append(0)
            else:
                val = stk.pop()
                stk[-1] += 2*val or 1 # assign the result 2*val if val == 0 assign 1 to stk[-1]
        return stk[0]


        