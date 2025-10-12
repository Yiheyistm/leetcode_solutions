class Solution:
    def isValid(self, s: str) -> bool:
        N = len(s)
        matched_parentheses = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in range(N):
            p = s[i]
            if p in "([{":
                stack.append(p)
            elif stack and matched_parentheses[stack[-1]] == p:
                stack.pop()
            else:
                return False

            if len(stack) > (N - i - 1):
                return False
            

        return True
        