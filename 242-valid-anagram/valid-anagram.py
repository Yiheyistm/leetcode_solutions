class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False

        my_dict = {}
        for ch in s:
            my_dict[ch] = my_dict.get(ch, 0) + 1 

        for ch in t:
            if ch in my_dict:
                my_dict[ch]-= 1
                if my_dict[ch] == 0:
                    del my_dict[ch]
            else:
                return False
        return not bool(my_dict)