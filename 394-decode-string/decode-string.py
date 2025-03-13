class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        for ch in s:
            if ch != ']':
                stack.append(ch)

            else:
                decoded_char = []
                decoded_digit = []
                while stack and stack[-1] != '[':
                    decoded_char.append(stack.pop())
                stack.pop()
                
                while stack and stack[-1].isdigit():
                    decoded_digit.append(stack.pop())
                
                decoded_str = ''.join(reversed(decoded_char))
                decoded_k = ''.join(reversed(decoded_digit))
                stack.append(decoded_str * int(decoded_k))
                
        return ''.join(stack)


        