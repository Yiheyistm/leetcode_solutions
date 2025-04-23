class Solution:
    def partitionString(self, s: str) -> int:
        mn = 1
        substr = ''
        for ch in s:
            if ch in substr :
                mn += 1
                substr = ''
            substr += ch
        return mn
        