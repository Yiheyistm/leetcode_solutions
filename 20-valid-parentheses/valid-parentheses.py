class Solution:
    def isValid(self, s: str) -> bool:
        pare_dict = {
            '(': ')',
            '{': '}', 
            '[': ']'
        }
        stack = []
        for par in s:
            
            if par in pare_dict:
                stack.append(par)
            elif stack and pare_dict[stack[-1]] == par:
                stack.pop()
            else:
                return False

        return stack == []
        