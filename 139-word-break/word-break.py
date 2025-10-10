class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
                    
        root = {}
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr["/"] = 1

        memo = [None] * len(s)
        def fn(i):
            if  i == len(s): return True
            if memo[i] == None:
                node = root
                memo[i] = False
                for j in range(i, len(s)):
                    ch = s[j]
                    if ch not in node:
                        break
                    node = node[ch]

                    if '/' in node and fn(j + 1):
                        memo[i] = True
                        break
            
            return memo[i]
        return fn(0) 







        