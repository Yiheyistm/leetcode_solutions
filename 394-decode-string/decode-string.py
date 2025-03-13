class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        for ch in s:
            if ch != ']':
                stack.append(ch)

            else:
                st = ''
                while stack and stack[-1] != '[':
                    st = stack.pop() + st

                stack.pop()
                n = ''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n

                stack.append(st * int(n))
        return ''.join(stack)


        