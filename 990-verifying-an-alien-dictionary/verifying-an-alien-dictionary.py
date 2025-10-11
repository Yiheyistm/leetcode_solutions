class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_order = {}
        for i, ch in enumerate(order):
            word_order[ch] = i
        sort_words = sorted(words, key=lambda x: [word_order[c] for c in x])
        return sort_words == words
        