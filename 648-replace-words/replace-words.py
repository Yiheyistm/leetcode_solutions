class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {}
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["end"] = 1
        
        sentence = sentence.split()
        last_sentence = []
        for word in sentence:
            i = 0
            node = root
            for ch in word:
                if ch not in node or "end" in node:
                    break
                node = node[ch]
                i += 1
            if "end" in node:
                last_sentence.append(word[:i])
            else:
                last_sentence.append(word)
        return " ".join(last_sentence)
        