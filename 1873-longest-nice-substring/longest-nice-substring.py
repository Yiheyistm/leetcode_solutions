class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def backtrack(s):
            
            if len(s) < 2: return ''
            
            check = set (s)

            for i in range(len(s)):
                if s[i].swapcase() not in check:
                    left = backtrack(s[:i])
                    right = backtrack(s[i+1:])
                    if len(left) >= len(right):
                        return left
                    else: return right
            return s
            
        return backtrack(s)
        