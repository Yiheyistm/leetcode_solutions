class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a','e', 'i','o','u'}
        s = list(s)
        vl_rev = []
        for ch in range(len(s) - 1, -1, -1):
            if s[ch].lower() in vowel:
                vl_rev.append(s[ch]) 

        i = 0
        res = []
        for j in range(len(s)):
            if s[j].lower() in vowel:
                res.append(vl_rev[i])
                i += 1
                continue
            res.append(s[j])
        return ''.join(res)
        