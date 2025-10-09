class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
            
        root = {}
        for word in wordDict:
            curr = root
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr["/"] = 1

        memo = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                return [""]
            if memo[i] == -1:
                node = root
                res = []
                for j in range(i, len(s)):
                    ch = s[j]
                    if ch not in node:
                        break
                    node = node[ch]
                    if '/' in node:
                        sub_sentence = dfs(j + 1)
                        for sub in sub_sentence:
                            if sub:
                                res.append(s[i:j +1] + " " + sub)
                            else:
                                res.append(s[i:j + 1])
                memo[i] = res
            return memo[i]
        return dfs(0)



        