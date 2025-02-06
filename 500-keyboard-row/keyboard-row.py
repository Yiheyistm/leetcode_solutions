class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f_row = set("qwertyuiop")
        s_row = set("asdfghjkl")
        t_row = set("zxcvbnm")
        res = []
        for word in words:
            if set(word.lower()).issubset(f_row) or set(word.lower()).issubset(s_row) or set  (word.lower()).issubset(t_row):
                res.append(word)
        return res


        