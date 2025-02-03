class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(s):
            return False
        for ch in s:
            if ch in s and ch in t:
                if s.count(ch) != t.count(ch):
                    return False
            if ch not in t:
                return False
        for ch in t:
            if ch not in s:
                return False
        return True