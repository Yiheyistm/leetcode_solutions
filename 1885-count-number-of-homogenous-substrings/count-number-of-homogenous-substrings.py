class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        substr = ''
        ans = 0
        for ch in s:
            if substr and substr[-1] != ch:
                ans =(ans +  len(substr) * (len(substr) +  1) // 2) % MOD
                substr = ''
            substr += ch
            
        if substr:
            ans =(ans +  len(substr) * (len(substr) +  1) // 2) % MOD
        return ans
        