from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch_ctr = Counter(chars)
        total = 0
        for word in words:
            is_formed = True
            w_ctr = Counter(word)
            for char in word:
                if w_ctr[char] > ch_ctr[char]:
                    is_formed = False
                    break
            
            total += len(word) if is_formed else 0
        return total


        