class Solution:
    def isValid(self, s: str) -> bool:
        matched_parentheses = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for p in s:
            if p in "([{":
                stack.append(p)
            elif p in ")]}" and stack:
                if matched_parentheses[stack[-1]] != p:
                    return False
                stack.pop()
            else:
                return False

        return True if not stack else False
        