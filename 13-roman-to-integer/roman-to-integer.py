class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0

        for i in range(len(s) - 1, -1, -1):
            if symbol[s[i]] > symbol[s[i-1]] and i > 0:
                res += symbol[s[i]] - symbol[s[i -1]]
                continue
            elif  i +1 < len(s) and symbol[s[i]] < symbol[s[i + 1]] :
                continue
            else:
                res += symbol[s[i]]
            print(res)
        return res
             
