class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = {}
        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["end"] = 1

        longest = ""
        def dfs(ch, node, word):
            nonlocal longest
            if "end" not in node[ch]:
                return
            word += ch
            for c in node[ch]:
                if c != "end":
                    dfs(c, node[ch], word)

            if len(word) > len(longest):
                longest = word
            elif len(word) == len(longest):
                longest = word if word < longest else longest


        for ch in root:
            dfs(ch, root, "")

        return longest
            
            
            
            

