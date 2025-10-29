class Solution:
    def countVowels(self, word: str) -> int:
        cnt = 0
        n = len(word)
        
        for i, ch in enumerate(word):
            if ch in "aeiou":
                cnt += (i + 1) * (n - i)
        return cnt

       

        