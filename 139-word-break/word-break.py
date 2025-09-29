class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        memo = [None] * len(s)
        def fn(i):
            if  i == len(s): return True
            if memo[i] == None:
                memo[i] = False
                for j in range(i, len(s)):
                    if s[i:j+1] in wd and fn(j + 1):
                        memo[i] = True
                        break
            
            return memo[i]
        return fn(0) 







        