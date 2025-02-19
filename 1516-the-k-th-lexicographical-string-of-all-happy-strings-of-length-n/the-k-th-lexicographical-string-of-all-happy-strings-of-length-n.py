class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        
        def backtrack(current_string):
            if len(current_string) == n:
                happy_strings.append(current_string)
                return
            for char in ['a', 'b', 'c']:
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)
        
        backtrack("")
        if len(happy_strings) < k:
            return ""
        
        return happy_strings[k-1]
        