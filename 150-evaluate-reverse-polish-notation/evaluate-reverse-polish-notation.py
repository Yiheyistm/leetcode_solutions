class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*':lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        for tok in tokens:
            if tok in operator:
                a = stack.pop()
                b = stack.pop()
                stack.append(operator[tok](b,a))
            else:
                stack.append(int(tok))
        return stack[0]
        