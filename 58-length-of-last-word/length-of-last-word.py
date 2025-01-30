class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = s.strip().split(' ')
        return len(str[-1])
        