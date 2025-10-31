class WordFilter:

    def __init__(self, words: List[str]):
        self.root = {} #(prefix, suffix) : index

        for i, word in enumerate(words):
            n = len(word)
            for p in range(n + 1):
                for s in range(n + 1):
                    suff = word[s:]
                    pref = word[:p]
                    key = pref + "#" + suff
                    node = self.root
                    for ch in key:
                        if ch not in node:
                            node[ch] = {}
                        node = node[ch]
                    node["idx"] = i

        

    def f(self, pref: str, suff: str) -> int:
        key = pref + "#" + suff
        node = self.root
        for ch in key:
            if ch not in node:
                return -1
            node = node[ch]
        return node.get("idx", -1)



    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)