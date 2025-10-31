class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = {}
        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
                node["pre"] = node.get("pre", 0) + 1


        res = []
        for word in words:
            cnt = 0
            node = root
            for ch in word:
                node = node[ch]
                cnt += node["pre"]
            res.append(cnt)
        return res
            
        