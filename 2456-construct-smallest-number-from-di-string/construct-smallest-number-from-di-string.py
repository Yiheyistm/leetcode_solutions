class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        current_digit = '1'
        
        for ch in pattern:
            stack.append(current_digit)
            current_digit = chr(ord(current_digit) + 1)
            if ch == 'I':
                while stack:
                    result.append(stack.pop())
        
        stack.append(current_digit)
        while stack:
            result.append(stack.pop())
        
        return ''.join(result)
        