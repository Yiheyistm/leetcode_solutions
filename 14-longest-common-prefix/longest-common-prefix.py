class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        root = {}
        for word in strs:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["end"] = 1
        
        prefix = ""
        start_word = strs[0] # choose whatever words
        node = root
        for ch in start_word:
            if "end" in node or len(node) > 1:break
            node = node[ch]
            prefix += ch
        return prefix
        

        