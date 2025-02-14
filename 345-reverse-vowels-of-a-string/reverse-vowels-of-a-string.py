class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a','e', 'i','o','u'}
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l].lower() not in vowel:
                l += 1
            while r > l and s[r].lower() not in vowel:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
        