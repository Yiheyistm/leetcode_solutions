class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["/"] = 1        

    def search(self, word: str) -> bool:
        word = [(word, self.root)]
        while word:
            pop_word, node = word.pop()
            for i, ch in enumerate(pop_word):
                if ch == '.':
                    for child in node:
                        if child != "/" and i + 1 < len(pop_word):
                            word.append((pop_word[i + 1:], node[child]))
                        if child != '/' and '/' in node[child] and i + 1 >= len(pop_word):
                            return True
                    break
                if ch not in node: break
                node = node[ch]
                if "/" in node and i + 1 == len(pop_word):
                    return True
                i += 1
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)