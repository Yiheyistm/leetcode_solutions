class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        str_dict = {}
        for char in s:
            str_dict[char] = str_dict.get(char, 0) + 1
        no_occurrence = s.count(s[0])
        
        return all(True if str_dict[ch] == no_occurrence else False for ch in s)
        