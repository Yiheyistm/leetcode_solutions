class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_order = {}
        for i, ch in enumerate(order):
            word_order[ch] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                ord1 = word_order[word1[j]]
                ord2 = word_order[word2[j]]

                if ord1 < ord2:
                    break
                elif ord2 < ord1:
                    return False
        return True


        