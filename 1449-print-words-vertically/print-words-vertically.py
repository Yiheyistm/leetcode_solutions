class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        max_str = len(max(s, key= len ))
        res_list = []
        for i in range(max_str):
            res = ""
            for j in range(len(s)):
                res += s[j][i] if len(s[j]) > i else " "
            if len(res.rstrip()):
                res_list.append(res.rstrip())
        
        return res_list

        