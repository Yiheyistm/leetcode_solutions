class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for ch in words:
            if set(ch).issubset(set(allowed)):
                count += 1
        return count

        